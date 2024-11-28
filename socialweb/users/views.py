from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, authenticate, logout
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib import messages
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


class profile_edit_view(UpdateView):
    model = Profile
    template_name = 'users/profile-edit.html'
    fields = ['first_name', 'last_name', 'avatar', 'proffecy', 'bg_PIC', 'location']
    success_url = reverse_lazy('main')


# class profile_delete_view(DeleteView):
#     model = Profile
#     template_name = 'users/deleteacc.html'
#     success_url = reverse_lazy('main')

def profile_delete_view(request):
    user = request.user

    if request.method == 'POST':
        logout(request)
        user.delete()
        messages.success(request, 'Account deleted, what a pity')
        return redirect('')

    return render(request, 'users/deleteacc.html')
