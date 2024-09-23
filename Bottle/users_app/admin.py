from django.contrib.admin import ModelAdmin,register
from .models import *
@register(UserProfile)
class UserProfileAdmin(ModelAdmin):
    pass