from django.contrib.admin import register,ModelAdmin
from .models import *

@register(Ranking)
class RankingAdmin(ModelAdmin):
    pass