from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate, login
from django.urls import reverse

from chatapp.views import index

def register(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        # MUST MATCH YOUR HTML FIELD NAMES
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm')

        # Validation
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return render(request, 'authentication/register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return render(request, 'authentication/register.html')

        # Create user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, "Account created successfully!")
        return redirect('login')

    return render(request, 'authentication/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('chatapp:index')
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'authentication/login.html')

def logout(request):
    if request.method == 'POST':
        logout(request)
    return render(request, 'authentication/logout.html')

def home(request):
    return render(request, 'authentication/home.html')
