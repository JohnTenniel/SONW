from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth import login, authenticate, logout
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib import messages
from .models import Profile
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import *
from django.db.models import Q


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


def profile_delete_view(request):
    user = request.user

    if request.method == 'POST':
        logout(request)
        user.delete()
        messages.success(request, 'Account deleted, what a pity')
        return redirect('main')

    return render(request, 'users/deleteacc.html')


class status_edit_view(UpdateView):
    model = Profile
    template_name = 'users/status-edit.html'
    fields = ['status']

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'pk': self.kwargs['pk']})


def invites_received_view(request):
    profile = Profile.objects.get(user=request.user)
    ph = Profile.objects.all()
    qs = Relationship.objects.invatations_received(profile)
    results = list(map(lambda x: x.sender, qs))
    is_empty = False
    if len(results) == 0:
        is_empty = True
    context = {'qs': results, 'profuser': ph, 'is_empty': is_empty}

    return render(request, 'users/my_invites.html', context)


def accept_invatation(request, pk):
    if request.method == 'POST':
        user = request.user
        sender = Profile.objects.get(pk=pk)
        receiver = Profile.objects.get(user=request.user)
        rel = get_object_or_404(Relationship, sender=sender, receiver=receiver)
        if rel.status == 'send':
            rel.status = 'accepted'
            rel.save()
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('users/profile')


def reject_invatation(request, pk):
    if request.method == 'POST':
        sender = Profile.objects.get(pk=pk)
        receiver = Profile.objects.get(user=request.user)
        rel = get_object_or_404(Relationship, sender=sender, receiver=receiver)
        rel.delete()
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('users/profile')


def profiles_list_view(request):
    user = request.user
    qs = Profile.objects.get_all_profiles(user)
    ph = Profile.objects.all()

    context = {'qs': qs, 'profuser': ph}

    return render(request, 'users/profile_list.html', context)


def invite_profiles_list_view(request):
    user = request.user
    ph = Profile.objects.all()
    qs = Profile.objects.get_all_profiles_to_invite(user)

    context = {'qs': qs, 'profuser': ph}

    return render(request, 'users/to_invite_list.html', context)


class ProfileListView(ListView):
    model = Profile
    template_name = 'users/profile_list.html'

    # context_object_name = 'qs'

    def get_queryset(self):
        qs = Profile.objects.get_all_profiles(self.request.user)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = User.objects.get(username__iexact=self.request.user)
        profile = Profile.objects.get(user=user)
        rel_r = Relationship.objects.filter(sender=profile)
        rel_s = Relationship.objects.filter(receiver=profile)
        rel_receiver = []
        rel_sender = []
        for item in rel_r:
            rel_receiver.append(item.receiver.user)
        for item in rel_s:
            rel_sender.append(item.sender.user)
        context['rel_receiver'] = rel_receiver
        context['rel_sender'] = rel_sender
        context['is_empty'] = False
        if len(self.get_queryset()) == 0:
            context['is_empty'] = True
        return context


def send_invatation(request, pk):
    if request.method == 'POST':
        user = request.user
        sender = Profile.objects.get(user=user)
        receiver = Profile.objects.get(pk=pk)

        rel = Relationship.objects.create(sender=sender, receiver=receiver, status='send')

        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('users/profile')


def remove_from_friends(request, pk):
    if request.method == 'POST':
        user = request.user
        sender = Profile.objects.get(user=user)
        receiver = Profile.objects.get(pk=pk)

        rel = Relationship.objects.get(
            (Q(sender=sender) & Q(receiver=receiver)) | (Q(sender=receiver) & Q(receiver=sender))
        )

        rel.delete()
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('users/profile')


