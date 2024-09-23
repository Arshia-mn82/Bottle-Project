from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def Register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("send_bottle")
    else:
        form = RegisterForm()
    return render(request, "users_app/register.html", {"form": form})
