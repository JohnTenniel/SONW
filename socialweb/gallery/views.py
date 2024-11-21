from django.shortcuts import render
from .models import Gallery, V_Gallery
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import *


def photo(request):
    ph = Gallery.objects.filter(autor_id=request.user.pk)
    context = {'g_imagine': ph}
    return render(request, "gallery/photo.html", context)


def video(request):
    vd = V_Gallery.objects.filter(autor_id=request.user.pk)
    context = {'g_video': vd}
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

