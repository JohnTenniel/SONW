from django.urls import path, include
from . import views
from .views import my_profile


urlpatterns = [
    path('profile/', my_profile, name='profile'),

]
