from django.urls import path
from .views import shop, buy_item, add_item_to_shop

urlpatterns = [
    path("shop/", shop, name="shop"),
    path("shop/buy/<int:item_id>/", buy_item, name="buy_item"),
    path("shop/add/", add_item_to_shop, name="add_item_to_shop"),
]