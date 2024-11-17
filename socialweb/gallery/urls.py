from django.urls import path, include
from . import views

urlpatterns = [
    path('photo/', views.photo, name='photo'),
    path('video/', views.video, name='video'),
]