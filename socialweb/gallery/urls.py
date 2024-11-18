from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('photo/', views.photo, name='photo'),
    path('video/', views.video, name='video'),
    path('addimage/', AddImage.as_view(), name='addimage'),
]
