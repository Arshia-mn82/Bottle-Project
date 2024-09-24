from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Bottle
from .forms import BottleForm
from django.views.decorators.csrf import csrf_exempt
from users_app.models import UserProfile
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

@csrf_exempt
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Logged in successfully!")
                return redirect('create_bottle')  # Redirect to bottle creation after login
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid login credentials.")
    else:
        form = AuthenticationForm()
    return render(request, "users_app/login.html", {"form": form})

@login_required
def create_bottle(request):
    # Check if the user has a UserProfile
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        messages.error(request, "User profile does not exist. Please register.")
        return redirect('register')  # Redirect to the register page if profile not found

    if request.method == "POST":
        form = BottleForm(request.POST)
        if form.is_valid():
            bottle = form.save(commit=False)
            bottle.sender = request.user
            
            # Set coordinates from the user's profile
            bottle.x = user_profile.x
            bottle.y = user_profile.y
            
            bottle.save()
            user_profile.coins += 10
            user_profile.save()
            messages.success(request, "Bottle sent successfully!")
            return redirect("bottle_list")
    else:
        form = BottleForm()

    return render(request, "bottles_app/create_bottle.html", {"form": form})

def bottle_list(request):
    bottles = Bottle.objects.all()
    return render(request, "bottles_app/bottle_list.html", {"bottles": bottles})
