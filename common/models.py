from django.db import models

class Values(models.Model):
  type = models.CharField(max_length=100, blank=True)
  sub_type = models.CharField(max_length=100, blank=True)
  value = models.CharField(max_length=100, blank=True)
  value_tw = models.CharField(max_length=100, blank=True)