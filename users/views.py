from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from users.models import Profile
from users.forms import ProfileForm

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
    """Update a user's profile view."""
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)

        if form.is_valid():
            data = form.cleaned_data

            profile.website = data['website']
            profile.phone_number = data['phone_number']
            profile.biography = data['biography']
            profile.picture = data['picture']
            profile.save()

            return redirect('update_profile')
    else:
        form = ProfileForm()

    return render(
        request=request,
        template_name='users/update_profile.html',
        context={
            'profile': profile,
            'user': request.user,
            'form': form
        }
    )
