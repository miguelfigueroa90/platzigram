from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

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
