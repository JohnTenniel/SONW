from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, CommentBlog, Reply
from .forms import BlogForm, CommentsForm, ReplyCreateForm
from django.views.generic import ListView, DetailView, CreateView, \
    UpdateView, DeleteView
from django.urls import reverse_lazy
from users.models import Profile
from django.views import View
from django.contrib.messages import Message


def blog(request):
    bg = Blog.objects.filter(autor_id=request.user.pk)
    ph = Profile.objects.all()
    context = {'blogpost': bg, 'profuser': ph}
    return render(request, "blog/mainblog.html", context)


#

class Article(View):
    def get(self, request, pk, *args, **kwargs):
        post = Blog.objects.get(pk=pk)
        ph = Profile.objects.all()
        form = CommentsForm()
        replyform = ReplyCreateForm()

        context = {
            'blogpost': post,
            'profuser': ph,
            'commentform': form,
            'replyform': replyform
        }

        return render(request, 'blog/Article.html', context)


def comment_sent(request, pk):
    post = get_object_or_404(Blog, id=pk)

    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid:
            comment = form.save(commit=False)
            comment.autor = request.user
            comment.post = post
            comment.save()

    return redirect('Article', post.id)


def reply_sent(request, pk):
    comment = get_object_or_404(CommentBlog, id=pk)

    if request.method == 'POST':
        form = ReplyCreateForm(request.POST)
        if form.is_valid:
            reply = form.save(commit=False)
            reply.autor = request.user
            reply.parent_comment = comment
            reply.save()

    return redirect('Article', comment.post.id)


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


def delet_comment(request, pk):
    post = get_object_or_404(CommentBlog, id=pk, autor=request.user)

    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Comment deleted')
        return redirect('Article', post.post.id)

    return render(request, 'blog/comment_delete.html', {'comment': post})


def delet_reply(request, pk):
    reply = get_object_or_404(Reply, id=pk, autor=request.user)

    if request.method == 'POST':
        reply.delete()
        messages.success(request, 'Reply deleted')
        return redirect('Article', reply.parent_comment.post.id)

    return render(request, 'blog/reply_delete.html', {'reply': reply})
