from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from users.forms import ProfileForm, SignupForm

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
    form = SignupForm()
    
    return render(request, 'users/signup.html', {'form': form})

def signup_user(request):
    form = SignupForm(request.POST)

    if form.is_valid():
        form.save()

        return redirect('login_form')

    return render(request, 'users/signup.html', {'form': form})

@login_required
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
