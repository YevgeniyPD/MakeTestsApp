from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)