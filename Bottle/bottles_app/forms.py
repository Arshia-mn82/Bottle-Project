from django import forms
from .models import Bottle

class BottleForm(forms.ModelForm):
    class Meta:
        model = Bottle
        fields = ['message'] 
