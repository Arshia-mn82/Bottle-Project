from django.shortcuts import render, redirect
from .models import BottleItem, Ability
from django.contrib import messages
from users_app.models import UserProfile

def shop(request):
    bottles = BottleItem.objects.all()
    abilities = Ability.objects.all()
    return render(request, "shop_app/shop.html", {"bottles": bottles, "abilities": abilities})

def buy_item(request, item_id):
    item = BottleItem.objects.get(id=item_id)
    user_profile = UserProfile.objects.get(user=request.user)

    if user_profile.coins >= item.price:
        user_profile.coins -= item.price
        user_profile.save()
        
        if item.name == "Respond Ability":
            user_profile.can_respond = True
            user_profile.save()

        messages.success(request, f"You have purchased {item.name} successfully!")
    else:
        messages.error(request, "Not enough coins.")
    return redirect("shop")

def add_item_to_shop(request):
    if request.method == "POST":
        name = request.POST.get('name')
        character_limit = request.POST.get('character_limit')
        range_limit = request.POST.get('range_limit')
        price = request.POST.get('price')
        
        BottleItem.objects.create(
            name=name,
            character_limit=character_limit,
            range_limit=range_limit,
            price=price
        )
        messages.success(request, "Item added to shop successfully!")
        return redirect("shop")
    return render(request, "shop_app/add_item_to_shop.html")