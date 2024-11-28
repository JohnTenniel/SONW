from django.urls import path, include
from . import views
from .views import my_profile, profile_edit_view, profile_delete_view


urlpatterns = [
    path('profile/<int:pk>', my_profile, name='profile'),

    # path('profile/edit/', profile_edit_view, name='profile-edit'),
    path('profile/edit/<int:pk>', profile_edit_view.as_view(), name='profile-edit'),
    # path('profile/delete/<int:pk>', profile_delete_view.as_view(), name='deleteacc'),
    path('profile/edit/', profile_delete_view, name='deleteacc')
]
