from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    path('', views.blog, name='blog'),
    path('Article/<int:pk>', Article.as_view(), name='Article'),
    path('Article/<int:pk>/like/', like_post, name='like-post'),
    path('comment/like/<pk>/', like_comment, name="like-comment"),
    path('reply/like/<pk>/', like_reply, name="like-reply"),
    path('commentsent/<pk>', comment_sent, name='comment-sent'),
    path('comment/delete/<pk>', delet_comment, name='comment-delete'),
    path('reply/<pk>', reply_sent, name='reply-sent'),
    path('reply/delete/<pk>', delet_reply, name='reply_delete'),
    path('addpost/', AddPostView.as_view(), name='addpost'),
    path('Article/edit/<int:pk>', UpdatePostView.as_view(), name='updatepost'),
    path('Article/<int:pk>/remove', DeletePostView.as_view(), name='deletepost'),
]
