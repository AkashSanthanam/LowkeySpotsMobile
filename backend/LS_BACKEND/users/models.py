from django.contrib.auth.models import AbstractUser
from django.db import models

class LowkeyUser(AbstractUser):
    map_count = models.IntegerField(default=0)
    friend_count = models.IntegerField(default=0)
