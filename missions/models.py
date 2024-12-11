from django.db import models
from django.contrib.postgres.fields import ArrayField
from users.models import User

class Mission(models.Model):
  # id = models.BigIntegerField(primary_key=True, auto_created=True)
  name = models.CharField(max_length=100, blank=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)# ForeignKey關聯到User
  start_date = models.DateTimeField(blank=True)
  end_date = models.DateTimeField(blank=True)
  salary_type = models.CharField(max_length=50, blank=True)
  salary = models.BigIntegerField(blank=True)
  currency = models.CharField(max_length=50, blank=True)
  location = models.CharField(max_length=100, blank=True)
  detail = models.CharField(max_length=4000, blank=True)
  skills = ArrayField(models.CharField(max_length=50, blank=True), blank=True)
  languages = ArrayField(models.JSONField(max_length=100, blank=True), blank=True)
