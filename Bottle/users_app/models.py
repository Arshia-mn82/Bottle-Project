from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    x = models.FloatField()
    y = models.FloatField()
    coins = models.IntegerField(default=100)
    bottles_read = models.IntegerField(default=0)
    daily_bottle_limit = models.IntegerField(default=3)

    def __str__(self) -> str:
        
        return self.user.username
