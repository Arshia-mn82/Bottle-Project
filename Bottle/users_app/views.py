from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .forms import CustomUserCreationForm
from .models import UserProfile

@csrf_exempt
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(
                user=user, x=form.cleaned_data["x"], y=form.cleaned_data["y"]
            )
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect("create_bottle")
        else:
            print(form.errors)
    else:
        form = CustomUserCreationForm()
    return render(request, "users_app/register.html", {"form": form})

@csrf_exempt
def register_success(request):
    return render(request, "users_app/register_success.html")

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("create_bottle")
    else:
        form = AuthenticationForm()
    return render(request, "users_app/login.html", {"form": form})
