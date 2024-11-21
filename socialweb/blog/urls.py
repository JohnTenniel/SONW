from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    # path('', blog.as_view(), name='blog'),
    path('', views.blog, name='blog'),
    path('Article/<int:pk>', Article.as_view(), name='Article'),
    path('addpost/', AddPostView.as_view(), name='addpost'),
    path('Article/edit/<int:pk>', UpdatePostView.as_view(), name='updatepost'),
    path('Article/<int:pk>/remove', DeletePostView.as_view(), name='deletepost'),
]
