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
            messages.success(request, "Registration successful!")
            return redirect("register_success")
        else:
            print(form.errors)
    else:
        form = CustomUserCreationForm()
    return render(request, "users_app/register.html", {"form": form})


@csrf_exempt
def register_success(request):
    return render(request, "users_app/register_success.html")
