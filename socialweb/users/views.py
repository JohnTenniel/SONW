from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, authenticate
from .models import Profile
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def my_profile(request):
    profile = Profile.objects.get(user=request.user)
    ph = Profile.objects.all()
    context = {'profile': profile, 'profuser': ph}
    return render(request, 'users/profile.html', context)





