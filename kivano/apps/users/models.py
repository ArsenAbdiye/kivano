from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    name = models.CharField(max_length=200, null=True, blank=True)  # Убрали unique=True
    password = models.CharField(max_length=128)  # Убрали unique=True и добавили max_length
