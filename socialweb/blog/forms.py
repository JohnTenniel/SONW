from django import forms
from .models import Blog, CommentBlog, Reply


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'photo']


class CommentsForm(forms.ModelForm):
    class Meta:
        model = CommentBlog
        fields = ['comment']
        widgets = {
            'comment': forms.TextInput(attrs={'placeholder': 'Add comment...'})
        }
        label = {
            'comment': ''
        }

class ReplyCreateForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['comment']
        widgets = {
            'comment': forms.TextInput(attrs={'placeholder': 'Add reply...', 'class': "!text-sm"})
        }
        label = {
            'comment': ''
        }