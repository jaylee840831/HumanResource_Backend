from django.urls import path
from . import views

urlpatterns = [
    path('create/user/', views.create_user, name='create_user'),
    path('update/user/<int:id>/', views.update_user, name='update_user'),
    path('update/user/<int:id>/password', views.update_password, name='update_password'),
    path('update/user/profile/<int:user_id>/', views.update_user_profile, name='update_user_profile'),
    path('get/user/<int:id>/', views.get_user, name='get_user'),
    path('get/user/profile/<int:user_id>/', views.get_user_profile, name='get_user_profile'),
    path('delete/user/<int:id>/', views.delete_user, name='delete_user')
]