from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    map_count = models.IntegerField(default=0)
    friend_count = models.IntegerField(default=0)