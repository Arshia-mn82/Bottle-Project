from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile


class CustomUserCreationForm(UserCreationForm):
    x = forms.FloatField(required=True, help_text="Enter X coordinate.")
    y = forms.FloatField(required=True, help_text="Enter Y coordinate.")

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "x", "y")
