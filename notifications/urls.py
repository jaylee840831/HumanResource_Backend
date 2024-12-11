from django.urls import path
from . import views

urlpatterns = [
  path('update/notify/<int:user_id>/', views.update_notification, name='update_notification'),
  path('get/notify/<int:user_id>/', views.get_notification, name='get_notification')
]