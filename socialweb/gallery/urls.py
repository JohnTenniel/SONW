from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('photo/', views.photo, name='photo'),
    path('hole_image/<int:pk>/', Image.as_view(), name='hole-image'),
    path('video/', views.video, name='video'),
    path('addimage/', AddImage.as_view(), name='addimage'),
    path('addvideo/', AddVideo.as_view(), name='addvideo'),
]
