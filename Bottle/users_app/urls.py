from django.urls import path
from .views import register, register_success, login_view  

urlpatterns = [
    path("register/", register, name="register"),
    path("register/success/", register_success, name="register_success"),
    path("login/", login_view, name="login"),  
]
