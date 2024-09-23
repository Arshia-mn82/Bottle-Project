from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def Register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  
            login(request, user)  
            messages.success(request, 'Registration successful!')
            return redirect('home')  
    else:
        form = UserCreationForm()
    return render(request, 'users_app/register.html', {'form': form})
