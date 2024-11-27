from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, \
    UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import *
from users.models import Profile
from django.views import View
from gallery.models import Gallery, V_Gallery, CommentIMG, CommentVG, ReplyIMG, ReplyVG
from django.http import HttpResponse
from django.contrib import messages


def photo(request):
    im = Gallery.objects.filter(autor_id=request.user.pk)
    ph = Profile.objects.all()
    context = {'g_imagine': im, 'profuser': ph}
    return render(request, "gallery/photo.html", context)


def video(request):
    vd = V_Gallery.objects.filter(autor_id=request.user.pk)
    ph = Profile.objects.all()
    context = {'g_video': vd, 'profuser': ph}
    return render(request, "gallery/videos.html", context)


class AddImage(CreateView):
    form_class = GaleryForm
    template_name = 'gallery/addimage.html'
    success_url = reverse_lazy('photo')

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.autor = self.request.user
        obj.save()
        return super().form_valid(form)


class AddVideo(CreateView):
    form_class = VideoForm
    template_name = 'gallery/addvideo.html'
    success_url = reverse_lazy('video')

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.autor = self.request.user
        obj.save()
        return super().form_valid(form)


class UpdateImage(CreateView):
    model = Gallery
    template_name = 'gallery/update_image.html'
    success_url = reverse_lazy('photo')


class DeleteIMG(DeleteView):
    model = Gallery
    template_name = 'gallery/deleteimg.html'
    success_url = reverse_lazy('photo')


class UpdateVideo(CreateView):
    model = V_Gallery
    template_name = 'gallery/update_video.html'
    success_url = reverse_lazy('videos')


class DeleteVG(DeleteView):
    model = V_Gallery
    template_name = 'gallery/deletevg.html'
    success_url = reverse_lazy('videos')


class Image(View):
    def get(self, request, pk, *args, **kwargs):
        post = Gallery.objects.get(pk=pk)
        ph = Profile.objects.all()
        form = CommentsIMGForm()
        replyform = ReplyIMGCreateForm()

        context = {
            'gpost': post,
            'profuser': ph,
            'commentimgform': form,
            'replyimgform': replyform
        }

        return render(request, 'gallery/hole-image.html', context)


def commentIMG_sent(request, pk):
    post = get_object_or_404(Gallery, id=pk)

    if request.method == 'POST':
        form = CommentsIMGForm(request.POST)
        if form.is_valid:
            comment = form.save(commit=False)
            comment.autor = request.user
            comment.post = post
            comment.save()

    return redirect('hole-image', post.id)


def replyIMG_sent(request, pk):
    comment = get_object_or_404(CommentIMG, id=pk)

    if request.method == 'POST':
        form = ReplyIMGCreateForm(request.POST)
        if form.is_valid:
            reply = form.save(commit=False)
            reply.autor = request.user
            reply.parent_comment = comment
            reply.save()

    return redirect('hole-image', comment.post.id)


def delet_commentimg(request, pk):
    post = get_object_or_404(CommentIMG, id=pk, autor=request.user)

    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Comment deleted')
        return redirect('hole-image', post.post.id)

    return render(request, 'gallery/comment_deletimg.html', {'comment': post})


def like_IMG(request, pk):
    post = get_object_or_404(Gallery, id=pk)
    user_exists = post.likes.filter(username=request.user.username).exists()

    if post.autor != request.user:
        if user_exists:
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

    return HttpResponse(post.likes.count())


def delet_replyimg(request, pk):
    reply = get_object_or_404(ReplyIMG, id=pk, autor=request.user)

    if request.method == 'POST':
        reply.delete()
        messages.success(request, 'Reply deleted')
        return redirect('hole-image', reply.parent_comment.post.id)

    return render(request, 'gallery/reply_deletimg.html', {'reply': reply})


def like_commentimg(request, pk):
    comment = get_object_or_404(CommentIMG, id=pk)
    user_exists = comment.likes.filter(username=request.user.username).exists()

    if comment.autor != request.user:
        if user_exists:
            comment.likes.remove(request.user)
        else:
            comment.likes.add(request.user)

    return HttpResponse(comment.likes.count())


def like_replyimg(request, pk):
    reply = get_object_or_404(ReplyIMG, id=pk)
    user_exists = reply.likes.filter(username=request.user.username).exists()

    if reply.autor != request.user:
        if user_exists:
            reply.likes.remove(request.user)
        else:
            reply.likes.add(request.user)

    return HttpResponse(reply.likes.count())


# _______________________VIDEO________________________________________
class Video(View):
    def get(self, request, pk, *args, **kwargs):
        post = V_Gallery.objects.get(pk=pk)
        ph = Profile.objects.all()
        form = CommentsVGForm()
        replyform = ReplyVGCreateForm()

        context = {
            'gpost': post,
            'profuser': ph,
            'commentvgform': form,
            'replyvgform': replyform
        }

        return render(request, 'gallery/hole-video.html', context)


def commentVG_sent(request, pk):
    post = get_object_or_404(V_Gallery, id=pk)

    if request.method == 'POST':
        form = CommentsVGForm(request.POST)
        if form.is_valid:
            comment = form.save(commit=False)
            comment.autor = request.user
            comment.post = post
            comment.save()

    return redirect('hole-video', post.id)


def replyVG_sent(request, pk):
    comment = get_object_or_404(CommentVG, id=pk)

    if request.method == 'POST':
        form = ReplyVGCreateForm(request.POST)
        if form.is_valid:
            reply = form.save(commit=False)
            reply.autor = request.user
            reply.parent_comment = comment
            reply.save()

    return redirect('hole-video', comment.post.id)


def delet_commentvg(request, pk):
    post = get_object_or_404(CommentVG, id=pk, autor=request.user)

    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Comment deleted')
        return redirect('hole-video', post.post.id)

    return render(request, 'gallery/comment_deletvg.html', {'comment': post})


def delet_replyvg(request, pk):
    reply = get_object_or_404(ReplyVG, id=pk, autor=request.user)

    if request.method == 'POST':
        reply.delete()
        messages.success(request, 'Reply deleted')
        return redirect('hole-video', reply.parent_comment.post.id)

    return render(request, 'gallery/reply_deletvg.html', {'reply': reply})


def like_VG(request, pk):
    post = get_object_or_404(V_Gallery, id=pk)
    user_exists = post.likes.filter(username=request.user.username).exists()

    if post.autor != request.user:
        if user_exists:
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

    return HttpResponse(post.likes.count())


def like_commentvg(request, pk):
    comment = get_object_or_404(CommentVG, id=pk)
    user_exists = comment.likes.filter(username=request.user.username).exists()

    if comment.autor != request.user:
        if user_exists:
            comment.likes.remove(request.user)
        else:
            comment.likes.add(request.user)

    return HttpResponse(comment.likes.count())


def like_replyvg(request, pk):
    reply = get_object_or_404(ReplyVG, id=pk)
    user_exists = reply.likes.filter(username=request.user.username).exists()

    if reply.autor != request.user:
        if user_exists:
            reply.likes.remove(request.user)
        else:
            reply.likes.add(request.user)

    return HttpResponse(reply.likes.count())
