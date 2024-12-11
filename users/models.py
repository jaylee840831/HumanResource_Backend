from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.postgres.fields import ArrayField

class User(AbstractUser):
  phone_number = models.CharField(max_length=20, blank=True)
  birth_date = models.DateTimeField(blank=True)

class User_Profile(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)# ForeignKey關聯到User
  experience = models.CharField(max_length=4000, blank=True)
  skills = ArrayField(models.CharField(max_length=50, blank=True), blank=True)
  languages = ArrayField(models.JSONField(max_length=100, blank=True), blank=True)