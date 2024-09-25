from django.urls import path
from .views import register, login_user,login_success, register_successful

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path('register_success/', register_successful, name='register_success'),
    path('login_success/', login_success, name='login_success'),
]