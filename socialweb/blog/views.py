from django.shortcuts import render
from .models import Blog
from .forms import BlogForm
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy


class blog(ListView):
    model = Blog
    template_name = 'blog/mainblog.html'


class Article(DetailView):
    model = Blog
    template_name = 'blog/Article.html'


class AddPostView(CreateView):
    form_class = BlogForm
    template_name = 'blog/addpost.html'
    success_url = reverse_lazy('blog')

