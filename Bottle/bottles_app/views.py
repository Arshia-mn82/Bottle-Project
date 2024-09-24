from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Bottle
from users_app.models import UserProfile


@login_required
def create_bottle(request):
    if request.method == "POST":
        message = request.POST.get("message")
        character_limit = request.POST.get("character_limit")
        range_limit = request.POST.get("range_limit")

        user_profile = UserProfile.objects.get(user=request.user)

        if user_profile.coins >= 10:
            bottle = Bottle.objects.create(
                message=message,
                character_limit=character_limit,
                range_limit=range_limit,
                sender=request.user,
            )
            user_profile.coins -= 10
            user_profile.save()
            messages.success(request, "Bottle sent successfully!")
            return redirect("bottle_list")
        else:
            messages.error(request, "Not enough coins to send a bottle.")

    return render(request, "bottles_app/create_bottle.html")


def bottle_list(request):
    bottles = Bottle.objects.all()
    user_profile = UserProfile.objects.get(user=request.user)
    visible_bottles = []

    for bottle in bottles:
        distance = (
            (user_profile.x - bottle.sender.profile.x) ** 2
            + (user_profile.y - bottle.sender.profile.y) ** 2
        ) ** 0.5
        if distance <= bottle.range_limit:
            visible_bottles.append(bottle)

    return render(request, "bottles_app/bottle_list.html", {"bottles": visible_bottles})


response_cost = 5  # Cost to respond to a bottle
reward_coins_read = 15  # Coins earned for reading a bottle


@login_required
def respond_to_bottle(request, bottle_id):
    bottle = Bottle.objects.get(id=bottle_id)
    user_profile = UserProfile.objects.get(user=request.user)

    distance = (
        (user_profile.x - bottle.sender.profile.x) ** 2
        + (user_profile.y - bottle.sender.profile.y) ** 2
    ) ** 0.5
    if user_profile.can_respond and distance <= bottle.range_limit:
        if request.method == "POST":
            response_message = request.POST.get("response_message")

            if user_profile.coins >= response_cost:
                user_profile.coins -= response_cost
                user_profile.save()

                messages.success(request, "Response sent successfully!")
                return redirect("bottle_list")
            else:
                messages.error(request, "You do not have enough coins to respond.")
                return redirect("bottle_list")

        return render(request, "bottles_app/respond_to_bottle.html", {"bottle": bottle})
    else:
        messages.error(
            request,
            "You need to purchase the ability to respond or you're not in range.",
        )
        return redirect("bottle_list")


@login_required
def read_bottle(request, bottle_id):
    bottle = Bottle.objects.get(id=bottle_id)
    user_profile = UserProfile.objects.get(user=request.user)

    user_profile.coins += reward_coins_read
    user_profile.save()

    messages.success(
        request, f"You earned {reward_coins_read} coins for reading this bottle!"
    )
    return render(request, "bottles_app/read_bottle.html", {"bottle": bottle})
