from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'templates/register.html')

        if User.objects.filter(username=email).exists():
            messages.error(request, 'Email already in use.')
            return render(request, 'templates/register.html')

        user = User.objects.create_user(username=email, password=password)
        auth_login(request, user)
        return redirect('/')

    return render(request, 'templates/register.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid email or password.')
            return render(request, 'templates/login.html')

    return render(request, 'templates/login.html')

def logout_view(request):
    return render(request, 'templates/login.html')
