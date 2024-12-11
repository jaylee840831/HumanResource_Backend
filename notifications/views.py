import logging
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.decorators import api_view
from .models import Notification
from .serializers import CustomNotificationSerializer

logger = logging.getLogger('main-logger')

@api_view(['PUT', 'PATCH'])
def update_notification(request, user_id, format=None):
  if request.method == 'PUT':
    try:
      notification = Notification.objects.get(user_id=user_id)
    except Notification.DoesNotExist:
      logger.error(f"Update failed, user {user_id}'s notification not found")
      raise NotFound(detail=f"User {user_id}'s notification not found")

    serializer = CustomNotificationSerializer(notification, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['GET'])
def get_notification(request, user_id, format=None):
  if request.method == 'GET':
    try:
      notification = Notification.objects.get(user_id=user_id)
    except Notification.DoesNotExist:
      logger.error(f"Get failed, user {user_id}'s notification not found")
      raise NotFound(detail=f"User {user_id}'s notification not found")

    serializer = CustomNotificationSerializer(notification)
    return Response(serializer.data, status=status.HTTP_200_OK)