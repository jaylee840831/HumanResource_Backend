import logging
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.exceptions import NotFound
from .models import User, User_Profile
from .serializers import CustomUserSerializer, CustomUserProfileSerializer
from rest_framework.permissions import AllowAny

logger = logging.getLogger('main-logger')

@api_view(['POST'])
@permission_classes([AllowAny])
def create_user(request):
  if request.method == 'POST':
    serializer = CustomUserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        logger.info(f"Create user {serializer.data}")
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    logger.error(f"Create failed, user {request.data} {serializer.errors}")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['PUT', 'PATCH'])
def update_user(request, id, format=None):
  if request.method == 'PUT':
    try:
      user = User.objects.get(id=id)
    except User.DoesNotExist:
      logger.error(f"Update failed, user {id} not found")
      raise NotFound(detail=f"User {id} not found")

    serializer = CustomUserSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        logger.info(f"Update user {serializer.data}")
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    logger.error(f"Update failed, user {id} {serializer.errors}")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['PUT', 'PATCH'])
def update_user_profile(request, user_id, format=None):
  if request.method == 'PUT':
    try:
      profile = User_Profile.objects.get(user_id = user_id)
    except User_Profile.DoesNotExist:
      logger.error(f"Get failed, user {user_id}'s profile not found")
      raise NotFound(detail=f"User {user_id}'s profile not found")
    
    serializer = CustomUserProfileSerializer(profile, data=request.data)
    if serializer.is_valid():
        serializer.save()
        logger.info(f"Update user profile {serializer.data}")
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    logger.error(f"Update user profile failed, user {id} {serializer.errors}")
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['PUT','PATCH'])
def update_password(request, id, format=None):
  if request.method == 'PUT':
    try:
      user = User.objects.get(id=id)
    except User.DoesNotExist:
      logger.error(f"Update failed, user {id} not found")
      raise NotFound(detail=f"User {id} not found")
    
    password = request.data.get('password')
    if password != '':
      user.set_password(password)
      user.save()
      logger.info(f"Update user {id}'s password successfully")
      return Response({'text':"Update user's password successfully"}, status=status.HTTP_200_OK)
    
    logger.error(f"Update user {id}'s password failed")
    return Response({'error':"Update user's password failed"}, status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['GET'])
def get_user(request, id, format=None):
  if request.method == 'GET':
    try:
      user = User.objects.get(id=id)
    except User.DoesNotExist:
      logger.error(f"Get failed, user {id} not found")
      raise NotFound(detail=f"User {id} not found")

    serializer = CustomUserSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
@api_view(['GET'])
def get_user_profile(request, user_id, format=None):
  if request.method == 'GET':
    try:
      profile = User_Profile.objects.get(user_id = user_id)
    except User_Profile.DoesNotExist:
      logger.error(f"Get failed, user {user_id}'s profile not found")
      raise NotFound(detail=f"User {user_id}'s profile not found")
    
    serializer = CustomUserProfileSerializer(profile)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
@api_view(['DELETE'])
def delete_user(request, id, format=None):
  if request.method == 'DELETE':
    try:
      user = User.objects.get(id=id)
    except User.DoesNotExist:
      logger.error(f"Delete failed, user {id} not found")
      raise NotFound(detail=f"User {id} not found")
    
    if user:
      user.delete()
      logger.info(f"Delete user {id}")
      return Response({'text':'User deleted successfully'}, status=status.HTTP_200_OK)
    
    logger.error(f"Delete failed, user {id}")
    return Response({'error':'User deleted error'}, status=status.HTTP_400_BAD_REQUEST)