from django.urls import path
from .views import *

urlpatterns = [
    path("register/", register, name="register"),
    path("register/success/", register_success, name="register_success"),
]
