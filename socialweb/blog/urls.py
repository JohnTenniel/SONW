from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('', blog.as_view(), name='blog'),
    path('Article/<int:pk>', Article.as_view(), name='Article'),
    path('addpost/', AddPostView.as_view(), name='addpost'),
]
