from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid
from users.models import Profile


class Blog(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    content = models.TextField(blank=True, verbose_name='Контент')
    photo = models.ImageField(upload_to="blog_photos/%Y/%m/%d/", blank=True, verbose_name='Фото')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    likes = models.ManyToManyField(User, related_name="likedposts", through="LikedPost")
    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    class Meta:
        ordering = ['-time_created']

    def __str__(self):
        return self.title


class CommentBlog(models.Model):
    comment = models.CharField(max_length=150)
    time_created = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comments')
    likes = models.ManyToManyField(User, related_name="likedcomments", through="LikedComment")
    name = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name='name')
    post = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        try:
            return f'{self.autor.username} : {self.comment[:30]}'
        except:
            return f'no author : {self.comment[:30]}'

    class Meta:
        ordering = ['-time_created']


class Reply(models.Model):
    comment = models.CharField(max_length=150)
    time_created = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='replies')
    name = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, related_name='namerep')
    likes = models.ManyToManyField(User, related_name='likedreplies', through='LikedReply')
    parent_comment = models.ForeignKey(CommentBlog, related_name='replies', on_delete=models.CASCADE)
    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        try:
            return f'{self.autor.username} : {self.comment[:30]}'
        except:
            return f'no author : {self.comment[:30]}'

    class Meta:
        ordering = ['time_created']


class LikedPost(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} : {self.post.title}'


class LikedComment(models.Model):
    comment = models.ForeignKey(CommentBlog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} : {self.comment.comment[:30]}'


class LikedReply(models.Model):
    reply = models.ForeignKey(Reply, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} : {self.reply.comment[:30]}'