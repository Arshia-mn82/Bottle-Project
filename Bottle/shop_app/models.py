from django.db import models

class BottleItem(models.Model):
    name = models.CharField(max_length=100)
    character_limit = models.IntegerField()
    range_limit = models.FloatField()
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Ability(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.name