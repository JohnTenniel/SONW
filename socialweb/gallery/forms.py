from django import forms
from .models import *
from django.contrib.auth.models import User


class GaleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['title', 'description', 'image']


class VideoForm(forms.ModelForm):
    class Meta:
        model = V_Gallery
        fields = ['title', 'description', 'video']
