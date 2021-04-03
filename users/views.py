from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from users.models import Profile

from django.db.utils import IntegrityError

def login_form(request):
    return render(request, 'users/login.html')

def login_authenticate(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)

        return redirect('feed')
    else:
        return render(request, 'users/login.html', {'error': 'Invalid username or password'})

@login_required
def logout_user(request):
    logout(request)

    return redirect('login_form')

def signup_form(request):
    return render(request, 'users/signup.html')

def signup_user(request):
    username = request.POST['username']
    password = request.POST['password']
    password_confirmation = request.POST['password_confirmation']

    if password_confirmation != password:
        return render(request, 'users/signup.html', {'error': 'Password confirmation does not match'})

    try:
        user = User.objects.create_user(username=username, password=password)
    except IntegrityError:
        return render(request, 'users/signup.html', {'error': 'Username is already in use'})

    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.email = request.POST['email']
    user.save()

    profile = Profile(user=user)
    profile.save()

    return redirect('login_form')

def update_profile(request):
    return render(request, 'users/update_profile.html')
