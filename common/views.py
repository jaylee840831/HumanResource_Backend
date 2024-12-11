from django.shortcuts import render
from django.core.cache import cache
from django_redis import get_redis_connection
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .serializers import CustomValuesSerializer
from .models import Values
import json

@api_view(['GET'])
def get_values(request, type):
  redis_key = 'common_data'
  redis_data = cache.get(redis_key)

  # redis如果沒有'common_data'的資料,從database拿資料並且緩存資料在redis,如果有就直接從redis拿
  if redis_data is None:
    print('data from db')
    try:
      values = Values.objects.filter(type = type)
      cache.delete(redis_key)
      storageValues = Values.objects.all()
      storageInRedis = CustomValuesSerializer(list(storageValues), many=True)
      cache.set(redis_key, json.dumps(storageInRedis.data), timeout=None)
    except Values.DoesNotExist:
      return Response({"error": "資料庫中無相關資料"}, status=404)
  else:
    print('data from redis')
    try:
      values = []
      # json.loads, 把JSON string解碼成Python object
      valuesFromRedis = json.loads(redis_data)
      for item in valuesFromRedis:
        if item['type'] == type:
          values.append(item)
    except:
      return Response({"error": "Redis中無相關資料"}, status=404)

  serializer = CustomValuesSerializer(list(values), many=True)
  return Response(serializer.data)

@api_view(['GET'])
def refresh_common_redis(request):
  redis_key = 'common_data'
  cache.delete(redis_key)

  try:
      values = Values.objects.all()
  except Values.DoesNotExist:
      return Response({"error": "資料庫中無相關資料"}, status=404)

  serializer = CustomValuesSerializer(list(values), many=True)
  # json.dumps, 把Python object編碼成JSON string
  cache.set(redis_key, json.dumps(serializer.data), timeout=None)

  return Response({"text": "Redis資料已更新"}, status=200)

@api_view(['GET'])
def get_all_redis_data(request):
  # 默認的 Redis 配置名稱是 "default"
  redis = get_redis_connection("default")

  # 查詢所有的鍵
  keys = redis.keys('*')

  # print(f"所有的鍵：{keys}")

  # for key in keys:
  #     value = redis.get(key)
  #     print(f"鍵: {key}, 值: {value}")

  return Response(keys, status=200)