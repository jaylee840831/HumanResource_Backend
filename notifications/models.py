from django.db import models
from users.models import User

class Notification(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)# ForeignKey關聯到User
  email = models.BooleanField(default=False)
  web = models.BooleanField(default=False)