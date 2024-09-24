from django.db import models
from django.contrib.auth.models import User

class Bottle(models.Model):
    message = models.TextField()
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    x = models.FloatField()
    y = models.FloatField()

    def __str__(self):
        return f"Bottle from {self.sender.username if self.sender else 'Anonymous'}"
