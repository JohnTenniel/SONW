from django.urls import path, include
from . import views
from .views import (
    my_profile,
    profile_edit_view,
    profile_delete_view,
    status_edit_view,
    invites_received_view,
    profiles_list_view,
    invite_profiles_list_view,
    ProfileListView,
    send_invatation,
    remove_from_friends,
    accept_invatation,
    reject_invatation,
)

urlpatterns = [
    path('profile/<int:pk>', my_profile, name='profile'),


    path('profile/edit/<int:pk>', profile_edit_view.as_view(), name='profile-edit'),
    path('status/edit/<int:pk>', status_edit_view.as_view(), name='status-edit'),
    path('profile/edit/', profile_delete_view, name='deleteacc'),
    path('my_invites/', invites_received_view, name='my_invites'),
    path('profile_list/', ProfileListView.as_view(), name='profile_list'),
    path('to_invite_list/', invite_profiles_list_view, name='to_invite_list'),
    path('to_invite_list/', invite_profiles_list_view, name='to_invite_list'),
    path('send_invate/<int:pk>', send_invatation, name='send-invate'),
    path('remove_friend/<int:pk>', remove_from_friends, name='remove-friend'),
    path('accept_invites/accept/<int:pk>', accept_invatation, name='accept-invite'),
    path('accept_invites/reject/<int:pk>', reject_invatation, name='reject-invite'),
]
