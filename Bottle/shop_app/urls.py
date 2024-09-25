from django.urls import path
from .views import shop, buy_item, add_item_to_shop
from bottles_app.views import create_bottle, bottle_list

urlpatterns = [
    path('shop/', shop, name='shop'),
    path('shop/buy_item/<int:item_id>/<str:item_type>/', buy_item, name='buy_item'),
    path('shop/add/', add_item_to_shop, name='add_item_to_shop'),
    path('bottle/create/', create_bottle, name='create_bottle'),
    path('bottle/list/', bottle_list, name='bottle_list'),
]
