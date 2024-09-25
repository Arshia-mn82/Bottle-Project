from django.shortcuts import render, redirect, get_object_or_404
from .models import BottleItem, Ability
from django.contrib import messages
from users_app.models import PurchasedItem, UserProfile, PurchasedAbility
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


def shop(request):
    bottles = BottleItem.objects.all()
    abilities = Ability.objects.all()
    user_profile = UserProfile.objects.get(user=request.user)

    return render(
        request,
        "shop_app/shop.html",
        {
            "bottles": bottles,
            "abilities": abilities,
            "user_profile": user_profile,
        },
    )


@login_required
def buy_item(request, item_id, item_type):
    if item_type == "bottle":
        item = get_object_or_404(BottleItem, id=item_id)
    elif item_type == "ability":
        item = get_object_or_404(Ability, id=item_id)
    else:
        messages.error(request, "Invalid item type.")
        return redirect("shop")

    user_profile = UserProfile.objects.get(user=request.user)

    if user_profile.coins >= item.price:
        user_profile.coins -= item.price
        user_profile.save()

        if item_type == "bottle":
            PurchasedItem.objects.create(user=request.user, item=item)

        elif item_type == "ability":
            PurchasedAbility.objects.create(user=request.user, ability=item)

            if item.name == "Bottle Infinite":
                user_profile.daily_bottle_limit = -1
            elif item.name == "Respond":
                user_profile.can_respond = True

            user_profile.save()

        messages.success(request, f"You have purchased {item.name} successfully!")
    else:
        messages.error(request, "Not enough coins.")

    return redirect("shop")


@csrf_exempt
def add_item_to_shop(request):
    if request.method == "POST":
        item_type = request.POST.get("item_type")
        name = request.POST.get("name")
        price = request.POST.get("price")

        try:
            price = float(price)

            if item_type == "bottle":
                character_limit = request.POST.get("character_limit")
                range_limit = request.POST.get("range_limit")

                if character_limit == "" or range_limit == "":
                    messages.error(
                        request, "Character limit and range limit cannot be empty."
                    )
                    return redirect("add_item_to_shop")

                BottleItem.objects.create(
                    name=name,
                    character_limit=int(character_limit),
                    range_limit=float(range_limit),
                    price=price,
                )
                messages.success(request, "Bottle Item added to shop successfully!")

            elif item_type == "ability":
                description = request.POST.get("description")

                if description == "":
                    messages.error(request, "Description cannot be empty.")
                    return redirect("add_item_to_shop")

                Ability.objects.create(name=name, description=description, price=price)
                messages.success(request, "Ability added to shop successfully!")

        except ValueError as e:
            messages.error(request, f"An error occurred: {e}")
            return redirect("add_item_to_shop")

        return redirect("shop")

    return render(request, "shop_app/add_item_to_shop.html")
