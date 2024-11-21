from django.shortcuts import render
from .models import Blog
from .forms import BlogForm
from django.views.generic import ListView, DetailView, CreateView, \
    UpdateView, DeleteView
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

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.autor = self.request.user
        obj.save()
        return super().form_valid(form)


class UpdatePostView(UpdateView):
    model = Blog
    template_name = 'blog/updatepost.html'
    fields = ['title', 'content', 'photo']
    success_url = reverse_lazy('blog')

class DeletePostView(DeleteView):
    model = Blog
    template_name = 'blog/deletepost.html'
    success_url = reverse_lazy('blog')