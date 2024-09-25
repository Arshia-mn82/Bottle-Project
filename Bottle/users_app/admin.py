from django.contrib.admin import ModelAdmin,register
from .models import *
@register(UserProfile)
class UserProfileAdmin(ModelAdmin):
    pass

@register(PurchasedItem)
class PurchasedItemAdmin(ModelAdmin):
    pass

@register(PurchasedAbility)
class PurchasedAbilityAdmin(ModelAdmin):
    pass