from rest_framework import serializers
from .models import Notification

class CustomNotificationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Notification
    # fields = '__all__'
    fields = ['user_id', 'email', 'web'] # 只序列化這些欄位資料

  def update(self, instance, validated_data):
    instance.email = validated_data.get('email', instance.email)
    instance.web = validated_data.get('web', instance.web)
    instance.save()
    return instance