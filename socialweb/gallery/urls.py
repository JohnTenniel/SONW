from django.urls import path, include
from . import views
from .views import *

urlpatterns = [
    # ______imagine______

    path('photo/', views.photo, name='photo'),
    path('addimage/', AddImage.as_view(), name='addimage'),
    path('hole_image/<int:pk>/', Image.as_view(), name='hole-image'),
    path('hole_image/edit/<int:pk>/', UpdateImage.as_view(), name='updateimg'),
    path('hole_image/remove/<int:pk>/', DeleteIMG.as_view(), name='deleteimg'),
    path('hole_image/like/<int:pk>/', like_IMG, name='like-img'),
    path('commentimg/like/<pk>/', like_commentimg, name="like-commentimg"),
    path('replyimg/like/<pk>/', like_replyimg, name="like-replyimg"),
    path('commentsentimg/<pk>', commentIMG_sent, name='commentimg-sent'),
    path('commentimg/delete/<pk>', delet_commentimg, name='commentimg-delete'),
    path('replyIMG/<pk>', replyIMG_sent, name='replyIMG-sent'),
    path('replyimg/delete/<pk>', delet_replyimg, name='replyimg_delete'),

    # ______video______

    path('video/', views.video, name='video'),
    path('addvideo/', AddVideo.as_view(), name='addvideo'),
    path('hole_video/<int:pk>/', Video.as_view(), name='hole-video'),
    path('hole_video/edit/<int:pk>/', UpdateVideo.as_view(), name='updatevg'),
    path('hole_video/remove/<int:pk>/', DeleteVG.as_view(), name='deletevg'),
    path('Article/<int:pk>/like/', like_VG, name='like-VG'),
    path('commentvg/like/<pk>/', like_commentvg, name="like-commentvg"),
    path('replyvg/like/<pk>/', like_replyvg, name="like-replyvg"),
    path('commentsentvg/<pk>', commentVG_sent, name='commentVG-sent'),
    path('commentvg/delete/<pk>', delet_commentvg, name='commentvg-delete'),
    path('replyVG/<pk>', replyVG_sent, name='replyVG-sent'),
    path('replyvg/delete/<pk>', delet_replyvg, name='replyvg_delete'),

]
