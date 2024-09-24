from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users_app.urls")),
    path("bottles/", include("bottles_app.urls")),
    path("shop/", include("shop_app.urls")),
]
