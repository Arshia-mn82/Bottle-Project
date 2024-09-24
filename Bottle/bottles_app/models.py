from django.db import models
from django.contrib.auth.models import User

class Bottle(models.Model):
    message = models.TextField()
    character_limit = models.IntegerField()
    range_limit = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='bottles')

    def __str__(self):
        return f"Bottle - Message: {self.message[:20]}..."