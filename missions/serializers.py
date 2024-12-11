from rest_framework import serializers
from .models import Mission

class CustomMissionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Mission
    fields = '__all__'

  def create(self, validated_data):
    mission = Mission.objects.create(**validated_data)
    mission.save()
    return mission
  
  # def update(self, instance, validated_data):
  #   instance.name = validated_data.get('name', instance.name)
  #   instance.start_date = validated_data.get('start_date', instance.start_date)
  #   instance.end_date = validated_data.get('end_date', instance.end_date)
  #   instance.is_active = validated_data.get('is_active', instance.is_active)
  #   instance.is_superuser = validated_data.get('is_superuser', instance.is_superuser)
  #   instance.birth_date = validated_data.get('birth_date', instance.birth_date)

  #   password = validated_data.pop('password', None)
  #   if password:
  #     instance.set_password(password)

  #   instance.save()
  #   return instance
