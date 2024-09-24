from django.urls import path
from .views import create_bottle, bottle_list, respond_to_bottle, read_bottle

urlpatterns = [
    path("bottles/create/", create_bottle, name="create_bottle"),
    path("bottles/", bottle_list, name="bottle_list"),
    path("bottles/respond/<int:bottle_id>/", respond_to_bottle, name="respond_to_bottle"),
    path("bottles/read/<int:bottle_id>/", read_bottle, name="read_bottle"),
]