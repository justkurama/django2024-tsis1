from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Follow
from .forms import ProfileForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile', pk=user.pk)
    else:
        form = UserCreationForm()
    return render(request, 'users/registration.html', {'form': form})

def profile(request, pk):
    user = get_object_or_404(User, pk=pk)
    profile = Profile.objects.get(user=user)
    return render(request, 'users/profile.html', {'profile': profile})

def edit_profile(request, pk):
    user = get_object_or_404(User, pk=pk)
    profile = Profile.objects.get(user=user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile', pk=user.pk)
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'users/edit_profile.html', {'form': form})

def follow_user(request, pk):
    user_to_follow = get_object_or_404(User, pk=pk)
    follow, created = Follow.objects.get_or_create(follower=request.user, following=user_to_follow)
    return redirect('profile', pk=user_to_follow.pk)

def unfollow_user(request, pk):
    user_to_unfollow = get_object_or_404(User, pk=pk)
    Follow.objects.filter(follower=request.user, following=user_to_unfollow).delete()
    return redirect('profile', pk=user_to_unfollow.pk)