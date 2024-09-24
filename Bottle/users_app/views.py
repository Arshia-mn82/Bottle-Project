from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.contrib.auth.models import User

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        x = request.POST.get('x')
        y = request.POST.get('y')

        user = User.objects.create_user(username=username, password=password)
        UserProfile.objects.create(user=user, x=x, y=y)
        messages.success(request, "Registration successful!")
        return redirect("login")
    return render(request, "users_app/register.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect("bottle_list")
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, "users_app/login.html")