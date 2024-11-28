from django.urls import path, include
from . import views
from .views import my_profile


urlpatterns = [
    path('profile/<int:pk>', my_profile, name='profile'),

]
