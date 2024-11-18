from django.shortcuts import render
from .models import Blog
from .forms import BlogForm
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy


# class blog(ListView):
#     model = Blog
#     template_name = 'blog/mainblog.html'

def blog(request):
    bg = Blog.objects.filter(autor_id=request.user.pk)
    context = {'blogpost': bg}
    return render(request, "blog/mainblog.html", context)




class Article(DetailView):
    model = Blog
    template_name = 'blog/Article.html'


class AddPostView(CreateView):
    form_class = BlogForm
    template_name = 'blog/addpost.html'
    success_url = reverse_lazy('blog')

