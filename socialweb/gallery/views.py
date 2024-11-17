from django.shortcuts import render
from .models import Gallery, V_Gallery


def photo(request):
    ph = Gallery.objects.filter(autor_id=request.user.pk)
    context = {'g_imagine': ph}
    return render(request, "gallery/photo.html", context)


def video(request):
    vd = V_Gallery.objects.filter(autor_id=request.user.pk)
    context = {'g_video': vd}
    return render(request, "gallery/videos.html", context)
