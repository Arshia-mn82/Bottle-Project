from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from rankings_app.models import Ranking
from shop_app.models import BottleItem
from .models import Bottle, Response
from users_app.models import PurchasedItem, UserProfile


@login_required
def create_bottle(request):
    if request.method == "POST":
        message = request.POST.get("message")

        user_profile = UserProfile.objects.get(user=request.user)
        purchased_items = PurchasedItem.objects.filter(user=request.user)

        for purchased in purchased_items:
            item = purchased.item
            if len(message) <= item.character_limit:
                bottle = Bottle.objects.create(
                    message=message,
                    character_limit=item.character_limit,
                    range_limit=item.range_limit,
                    sender=request.user,
                )
                messages.success(request, "Bottle sent successfully!")
                return redirect("bottle_list")

        messages.error(request, "You do not have a valid bottle item.")
    return render(request, "bottles_app/create_bottle.html")


@login_required
def bottle_list(request):
    bottles = Bottle.objects.exclude(sender=request.user)
    user_profile = UserProfile.objects.get(user=request.user)
    visible_bottles = []

    for bottle in bottles:
        if bottle.sender and hasattr(bottle.sender, "profile"):
            distance = (
                (user_profile.x - bottle.sender.profile.x) ** 2
                + (user_profile.y - bottle.sender.profile.y) ** 2
            ) ** 0.5
            if distance <= bottle.range_limit:
                visible_bottles.append(bottle)

    return render(request, "bottles_app/bottle_list.html", {"bottles": visible_bottles})


response_cost = 5
reward_coins_read = 15


@login_required
def respond_to_bottle(request, bottle_id):
    original_bottle = Bottle.objects.get(id=bottle_id)
    user_profile = UserProfile.objects.get(user=request.user)

    if (
        original_bottle.sender
        and original_bottle.sender.profile
        and user_profile.coins >= response_cost
    ):
        distance = (
            (user_profile.x - original_bottle.sender.profile.x) ** 2
            + (user_profile.y - original_bottle.sender.profile.y) ** 2
        ) ** 0.5

        if user_profile.can_respond and distance <= original_bottle.range_limit:
            if request.method == "POST":
                response_message = request.POST.get("response_message")

                response_bottle = Bottle.objects.create(
                    message=response_message,
                    character_limit=original_bottle.character_limit,
                    range_limit=original_bottle.range_limit,
                    sender=request.user,
                )

                messages.success(request, "Response sent successfully!")
                return redirect("bottle_list")
            return render(
                request,
                "bottles_app/respond_to_bottle.html",
                {"bottle": original_bottle},
            )
        else:
            messages.error(
                request,
                "You need to purchase the ability to respond or you're not in range.",
            )
            return redirect("bottle_list")
    else:
        messages.error(request, "Sender information is missing.")
        return redirect("bottle_list")


@login_required
@login_required
def read_bottle(request, bottle_id):
    bottle = Bottle.objects.get(id=bottle_id)
    user_profile = UserProfile.objects.get(user=request.user)

    
    user_profile.coins += reward_coins_read
    user_profile.bottles_read += 1  
    user_profile.save()

    
    ranking, created = Ranking.objects.get_or_create(user_profile=user_profile)
    ranking.bottles_read += 1  
    ranking.save()

    messages.success(
        request, f"You earned {reward_coins_read} coins for reading this bottle!"
    )

    
    return render(request, "bottles_app/read_bottle.html", {"bottle": bottle})
