from django.db import models
from django.contrib.auth.models import User
import uuid


class Gallery(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(default="default1.jpg", upload_to="GIMG/%Y/%m/%d")
    demo_link = models.CharField(max_length=200, blank=True)
    source_link = models.CharField(max_length=200, blank=True)
    tags = models.ManyToManyField('Album', blank=True)
    vote_total = models.IntegerField(default=0, blank=True)
    vote_ratio = models.IntegerField(default=0, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    likes = models.ManyToManyField(User, related_name="likedimg", through="LikedIMG")

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title


class V_Gallery(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    video = models.FileField(default="default.mov", upload_to="GVD/%Y/%m/%d")
    demo_link = models.CharField(max_length=200, blank=True)
    source_link = models.CharField(max_length=200, blank=True)
    tags = models.ManyToManyField('Album', blank=True)
    vote_total = models.IntegerField(default=0, blank=True)
    vote_ratio = models.IntegerField(default=0, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    likes = models.ManyToManyField(User, related_name="likedvg", through="LikedVG")

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title


class Album(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class CommentIMG(models.Model):
    comment = models.CharField(max_length=150)
    time_created = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='commentsimg')
    likes = models.ManyToManyField(User, related_name="likedcommentsimg", through="LikedCommentIMG")
    post = models.ForeignKey(Gallery, related_name='commentsimg', on_delete=models.CASCADE)
    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        try:
            return f'{self.autor.username} : {self.comment[:30]}'
        except:
            return f'no author : {self.comment[:30]}'

    class Meta:
        ordering = ['-time_created']


class CommentVG(models.Model):
    comment = models.CharField(max_length=150)
    time_created = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='commentsvg')
    likes = models.ManyToManyField(User, related_name="likedcommentsvg", through="LikedCommentVG")
    post = models.ForeignKey(V_Gallery, related_name='commentsvg', on_delete=models.CASCADE)
    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        try:
            return f'{self.autor.username} : {self.comment[:30]}'
        except:
            return f'no author : {self.comment[:30]}'

    class Meta:
        ordering = ['-time_created']


class ReplyIMG(models.Model):
    comment = models.CharField(max_length=150)
    time_created = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='repliesimg')
    likes = models.ManyToManyField(User, related_name='likedrepliesimg', through='LikedReplyIMG')
    parent_comment = models.ForeignKey(CommentIMG, related_name='repliesimg', on_delete=models.CASCADE)
    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        try:
            return f'{self.autor.username} : {self.comment[:30]}'
        except:
            return f'no author : {self.comment[:30]}'

    class Meta:
        ordering = ['time_created']


class ReplyVG(models.Model):
    comment = models.CharField(max_length=150)
    time_created = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='repliesvg')
    likes = models.ManyToManyField(User, related_name='likedrepliesvg', through='LikedReplyVG')
    parent_comment = models.ForeignKey(CommentVG, related_name='repliesvg', on_delete=models.CASCADE)
    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        try:
            return f'{self.autor.username} : {self.comment[:30]}'
        except:
            return f'no author : {self.comment[:30]}'

    class Meta:
        ordering = ['time_created']


class LikedIMG(models.Model):
    post = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="LikedIMGUS")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} : {self.post.title}'


class LikedVG(models.Model):
    post = models.ForeignKey(V_Gallery, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="LikedVGUS")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} : {self.post.title}'


class LikedCommentIMG(models.Model):
    comment = models.ForeignKey(CommentIMG, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} : {self.comment.comment[:30]}'


class LikedCommentVG(models.Model):
    comment = models.ForeignKey(CommentVG, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} : {self.comment.comment[:30]}'


class LikedReplyIMG(models.Model):
    reply = models.ForeignKey(ReplyIMG, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} : {self.reply.comment[:30]}'


class LikedReplyVG(models.Model):
    reply = models.ForeignKey(ReplyVG, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} : {self.reply.comment[:30]}'
