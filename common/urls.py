from django.urls import path
from . import views

urlpatterns = [
  path('get/values/<str:type>/', views.get_values, name='get_values'),
  path('redis/data/common/refresh/', views.refresh_common_redis, name='refresh_common_redis'),
  path('redis/data/all/', views.get_all_redis_data, name='get_all_redis_data')
]