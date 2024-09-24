from django.db import models
from users_app.models import UserProfile

class Ranking(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    bottles_read = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user_profile.user.username} - {self.bottles_read} Bottles Read"