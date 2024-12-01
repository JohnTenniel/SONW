from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from .models import *


class ProfileEdit(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'avatar',
                  'proffecy', 'bg_PIC', 'location']


class StatusEdit(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['status']
