from django.urls import path
from .views import create_bottle, bottle_list, login_view

urlpatterns = [
    path("bottles/create/", create_bottle, name="create_bottle"),
    path("bottles/", bottle_list, name="bottle_list"),
    path("login/", login_view, name="login"),  
]
