from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from .models import Mission
from .serializers import CustomMissionSerializer
from common.serializers import CustomValuesSerializer
from common.models import Values

@api_view(['POST'])
def create_mission(request):
  if request.method == 'POST':
    serializer = CustomMissionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['PUT', 'PATCH'])
def update_mission(request, id, format=None):
  if request.method == 'PUT':
    try:
      mission = Mission.objects.get(id=id)
    except Mission.DoesNotExist:
      raise NotFound(detail=f"Mission {id} not found")

    serializer = CustomMissionSerializer(mission, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['POST'])
def get_missions(request):
  if request.method == 'POST':
    # 條件篩選
    try:
      if request.data.get('search_keyword') == '':
        missions = Mission.objects.all().order_by('-start_date')
      else:
        missions = Mission.objects.filter(
        Q(name__icontains=request.data.get('search_keyword')) |
        Q(location__icontains=request.data.get('search_keyword'))
        # Q(skills__contains=[request.data.get('search_keyword')])
        # Q(languages__contains={ 'value_tw':request.data.get('search_keyword')})
        ).order_by('-start_date')
    except Mission.DoesNotExist:
      raise NotFound(detail=f"Mission {id} not found")

    # 分頁
    try:
      paginator = Paginator(missions, 5)
      page = paginator.page(request.data.get('page'))
    except EmptyPage:
      return Response({'missions':[], 'total': missions.count()}, status=status.HTTP_200_OK)

    serializer = CustomMissionSerializer(list(page.object_list.values()), many=True)
    timeSerializer = CustomValuesSerializer(Values.objects.filter(type = 'time'), many=True)
    currencySerializer = CustomValuesSerializer(Values.objects.filter(type = 'currency'), many=True)
    skillSerializer = CustomValuesSerializer(Values.objects.filter(type = 'skill'), many=True)
    languageSerializer = CustomValuesSerializer(Values.objects.filter(type = 'language'), many=True)

    for data in serializer.data:
      data['salary_type'] = [item['value_tw'] for item in timeSerializer.data if item['value'] == data.get('salary_type', '')][0]
      data['currency'] = [item['value_tw'] for item in currencySerializer.data if item['value'] == data.get('currency', '')][0]

      newSkills = []
      for s in data['skills']:
        for ss in skillSerializer.data:
          if s == ss['value']:
            newSkills.append(ss['value_tw'])
      data['skills'] = newSkills

      newLanguages = []
      for l in data['languages']:
        for ll in languageSerializer.data:
          if l['lan'] == ll['value']:
            newLanguages.append({
              'lan': ll['value_tw'],
              'level': l['level']
            })
      data['languages'] = newLanguages

    return Response({'missions':serializer.data, 'total': missions.count()}, status=status.HTTP_200_OK)
  
@api_view(['DELETE'])
def delete_mission(request, id, format=None):
  if request.method == 'DELETE':
    try:
      mission = Mission.objects.get(id=id)
    except Mission.DoesNotExist:
      raise NotFound(detail=f"Mission {id} not found")
    
    if mission:
      mission.delete()
      return Response({'text':'Mission deleted successfully'}, status=status.HTTP_200_OK)
    return Response({'error':'Mission deleted error'}, status=status.HTTP_400_BAD_REQUEST)