from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, authenticate
from .models import *
from django.urls import reverse_lazy


def send_request(request, id):
    from_user = request.User
    to_user = User.objects.get(id=id)
    request = FriendRequest.objects.get_or_create(from_user=from_user, to_user=to_user)
    return redirect('')

def accept_request(request,id):
    frequest = FriendRequest.objects.get(id=id)
    user1 = request.User
    user2 = frequest.from_user
    user1.friends.add(user2)
    user2.friends.add(user1)
    return redirect('')