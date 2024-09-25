from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm


def register_successful(request):
    return render(request, "users_app/register_success.html")


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            x = form.cleaned_data["x"]
            y = form.cleaned_data["y"]

            UserProfile.objects.create(user=user, x=x, y=y)
            messages.success(request, "Registration successful!")
            return redirect("register_success")
    else:
        form = CustomUserCreationForm()

    return render(request, "users_app/register.html", {"form": form})


def login_success(request):
    return render(request, "users_app/login_success.html")


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("login_success")
        else:
            messages.error(request, "Invalid username or password. Please register.")
            return redirect("register")
    return render(request, "users_app/login.html")
