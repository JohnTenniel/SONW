from django.contrib import admin
from .models import Blog, CommentBlog, Reply

admin.site.register(Blog)
admin.site.register(CommentBlog)
admin.site.register(Reply)
