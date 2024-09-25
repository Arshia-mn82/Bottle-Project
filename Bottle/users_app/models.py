from django.contrib.auth.models import User
from django.db import models
from shop_app.models import BottleItem, Ability

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE , related_name='profile')
    x = models.FloatField()
    y = models.FloatField()
    coins = models.IntegerField(default=100)
    bottles_read = models.IntegerField(default=0)
    daily_bottle_limit = models.IntegerField(default=3)
    can_respond = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}'s profile"
    
    
class PurchasedItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(BottleItem, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} purchased {self.item.name}"
    
class PurchasedAbility(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ability = models.ForeignKey(Ability, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} purchased {self.ability.name}"