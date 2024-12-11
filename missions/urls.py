from django.urls import path
from . import views

urlpatterns = [
    path('create/mission/', views.create_mission, name='create_mission'),
    path('update/mission/<int:id>/', views.update_mission, name='update_mission'),
    path('get/missions/', views.get_missions, name='get_missions'),
    path('delete/mission/<int:id>/', views.delete_mission, name='delete_mission')
]