from django.urls import path, include
from . import views
from .views import my_profile, profile_edit_view


urlpatterns = [
    path('profile/<int:pk>', my_profile, name='profile'),

    path('profile/edit/', profile_edit_view, name='profile-edit'),

]
