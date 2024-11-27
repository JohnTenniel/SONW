from django.shortcuts import render, redirect
from django.views import View
from .forms import UserCreationForm
from django.contrib.auth import login, authenticate
from itertools import chain
from users.models import Profile
from gallery.models import Gallery, V_Gallery
from blog.models import Blog, CommentBlog, Reply
from django.core.paginator import Paginator
import random
import operator


# import random
# random

def main(request):
    ph = Profile.objects.all()
    gl = Gallery.objects.all()
    vd = V_Gallery.objects.all()
    bg = Blog.objects.all()
    cb = CommentBlog.objects.all()
    # ch = list(chain(Gallery.objects.all(), V_Gallery.objects.all(), Blog.objects.all()))
    ch = list(chain(gl, vd, bg))
    ch = sorted(ch, key=operator.attrgetter('created'), reverse=True)
    context = {'profuser': ph, 'gall': gl, 'vgall': vd, 'mblog': bg, 'changemain': ch, 'cbl': cb, }
    return render(request, "main/main.html", context)


def test(request):
    ph = Profile.objects.all()
    bg = Blog.objects.all()
    fr = ph.sender.all()
    context = {'profuser': ph, 'mblog': bg, 'fr': fr}
    return render(request, "main/test.html", context)

def last(request):
    ph = Profile.objects.all()
    gl = Gallery.objects.all()
    vd = V_Gallery.objects.all()
    bg = Blog.objects.all()
    cb = CommentBlog.objects.all()
    # ch = list(chain(Gallery.objects.all(), V_Gallery.objects.all(), Blog.objects.all()))
    ch = list(chain(gl, vd, bg))
    ch = sorted(ch, key=operator.attrgetter('created'), reverse=True)

    # paginator = Paginator(ch, 3)
    # page = int(request.GET.get('page', 1))
    # ch = paginator.page(page)

    context = {'profuser': ph, 'gall': gl, 'vgall': vd, 'mblog': bg, 'changemain': ch, 'cbl': cb}

    # if request.htmx:
    #     return render(request, "snippets/looplastnwes.html", context)

    return render(request, "main/last_news.html", context)



class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('main')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)
