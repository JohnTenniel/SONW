from django.contrib import admin
from .models import Blog, CommentBlog, Reply, LikedPost, LikedComment, LikedReply

admin.site.register(Blog)
admin.site.register(CommentBlog)
admin.site.register(Reply)
admin.site.register(LikedPost)
admin.site.register(LikedComment)
admin.site.register(LikedReply)
