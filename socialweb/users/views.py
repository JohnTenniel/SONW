from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView

from .models import Profile
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import *


@login_required
def my_profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    ph = Profile.objects.all()
    context = {'profile': profile, 'profuser': ph}
    return render(request, 'users/profile.html', context)


def profile_edit_view(request):
    form = ProfileEdit()
    profile = Profile.objects.all()
    ph = Profile.objects.all()
    context = {'profile': profile, 'profuser': ph, 'form': form}

    if request.method == 'POST':
        form = ProfileEdit(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    return render(request, 'users/profile-edit.html', context)


