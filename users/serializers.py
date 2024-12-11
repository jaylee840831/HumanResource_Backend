from django.contrib.auth import password_validation
from rest_framework import serializers
from .models import User, User_Profile
from notifications.models import Notification

class CustomUserSerializer(serializers.ModelSerializer):
  password = serializers.CharField(write_only=True, required=False) # 密碼欄位只允許寫入，且不一定要寫入

  class Meta:
    model = User
    fields = '__all__'
    # fields = ['username', 'password', 'email', 'phone_number', 'birth_date'] # 只序列化這些欄位資料

  def create(self, validated_data):
    user = User.objects.create(**validated_data)

    password = validated_data.pop('password')
    if password:
      user.set_password(password)

    user.save()

    # 新增user,順便新增user profile、notification
    profile_exists = User_Profile.objects.filter(user=user).exists()
    if not profile_exists:
      user_profile = User_Profile.objects.create(
        user=user,
        skills=[],
        languages=[]
      )

    notification_exists = Notification.objects.filter(user=user).exists()
    if not notification_exists:
      notification = Notification.objects.create(
        user=user,
        email=True,
        web=True
      )

    return user
  
  def update(self, instance, validated_data):
    instance.username = validated_data.get('username', instance.username)
    instance.phone_number = validated_data.get('phone_number', instance.phone_number)
    instance.email = validated_data.get('email', instance.email)
    instance.is_active = validated_data.get('is_active', instance.is_active)
    instance.is_superuser = validated_data.get('is_superuser', instance.is_superuser)
    instance.birth_date = validated_data.get('birth_date', instance.birth_date)

    password = validated_data.pop('password', None)
    if password:
      instance.set_password(password)

    instance.save()
    return instance

class CustomUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
      model = User_Profile
      # fields = '__all__'
      fields = ['experience', 'skills', 'languages', 'user_id']

    def update(self, instance, validated_data):
      instance.experience = validated_data.get('experience', instance.experience)
      instance.skills = validated_data.get('skills', instance.skills)
      instance.languages = validated_data.get('languages', instance.languages)
      instance.save()
      return instance