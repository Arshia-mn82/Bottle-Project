from django.contrib.admin import register,ModelAdmin
from .models import *

@register(Bottle)
class BottleAdmin(ModelAdmin):
    pass

@register(Response)
class ResponseAdmin(ModelAdmin):
    pass


