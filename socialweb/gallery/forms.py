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


class CommentsIMGForm(forms.ModelForm):
    class Meta:
        model = CommentIMG
        fields = ['comment']
        widgets = {
            'comment': forms.TextInput(attrs={'placeholder': 'Add comment...'})
        }
        label = {
            'comment': ''
        }


class ReplyIMGCreateForm(forms.ModelForm):
    class Meta:
        model = ReplyIMG
        fields = ['comment']
        widgets = {
            'comment': forms.TextInput(attrs={'placeholder': 'Add reply...', 'class': "!text-sm"})
        }
        label = {
            'comment': ''
        }


class CommentsVGForm(forms.ModelForm):
    class Meta:
        model = CommentVG
        fields = ['comment']
        widgets = {
            'comment': forms.TextInput(attrs={'placeholder': 'Add comment...'})
        }
        label = {
            'comment': ''
        }


class ReplyVGCreateForm(forms.ModelForm):
    class Meta:
        model = ReplyVG
        fields = ['comment']
        widgets = {
            'comment': forms.TextInput(attrs={'placeholder': 'Add reply...', 'class': "!text-sm"})
        }
        label = {
            'comment': ''
        }
