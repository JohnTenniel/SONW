from django import forms
from .models import *
from django.contrib.auth.models import User


class GaleryForm(forms.ModelForm):

    class Meta:
        model = Gallery
        fields = ['title', 'description', 'image']

