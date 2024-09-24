from django import forms
from .models import Bottle
from shop_app.models import ShopItem

class BottleForm(forms.ModelForm):
    class Meta:
        model = Bottle
        fields = ['message'] 

class ShopItemSelectionForm(forms.Form):
    item = forms.ModelChoiceField(queryset=ShopItem.objects.all(), label="Select a bottle type")