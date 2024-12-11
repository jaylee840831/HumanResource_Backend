import logging
from django.shortcuts import render
# from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.exceptions import NotFound
from users.models import User
from rest_framework.permissions import AllowAny

logger = logging.getLogger('main-logger')

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
  email = request.data.get('email')
  password = request.data.get('password')

  try:
    user = User.objects.get(email=email)
    if user is None:
      logger.error('Login failed, user not found: ' + email)
      return Response({'error': 'Login failed'}, status=status.HTTP_401_UNAUTHORIZED)
    elif user.check_password(password) == False:
      logger.error('Login failed, password error: ' + email)
      return Response({'error': 'Login failed'}, status=status.HTTP_401_UNAUTHORIZED)
    else:
      logger.info('Login: ' + email)
      refresh = RefreshToken.for_user(user)
      return Response({
        'user_id': str(user.id),
        'username': str(user.username),
        'refresh_token': str(refresh),
        'access_token': str(refresh.access_token),
      })
  except User.DoesNotExist:
    logger.error('Login failed, ' + email)
    return Response({'error': 'Login failed'}, status=status.HTTP_401_UNAUTHORIZED)
