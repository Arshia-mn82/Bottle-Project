from django.contrib.admin import register,ModelAdmin
from .models import *

@register(BottleItem)
class BottleItemAdmin(ModelAdmin):
    pass

@register(Ability)
class AbilityAdmin(ModelAdmin):
    pass