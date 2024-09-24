from django.urls import path
from .views import ranking_view

urlpatterns = [
    path("rankings/", ranking_view, name="rankings"),
]