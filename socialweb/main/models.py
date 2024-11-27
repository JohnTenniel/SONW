from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    class Meta:
        db_table = "MainProfile"

    user = models.OneToOneField('Profile', on_delete=models.CASCADE, related_name='nameuser')
    first_name = models.CharField('Profile', max_length=150, blank=True)
    last_name = models.CharField('Profile', max_length=150, blank=True)
    email = models.EmailField('Profile', blank=True)
    is_staff = models.BooleanField('Profile', default=False)
    is_active = models.BooleanField('Profile', default=True)
    middle_name = models.CharField('Profile', max_length=50, blank=True)
    phone = models.CharField('Profile', max_length=14, blank=True)
    avatar = models.ImageField('Profile', upload_to="prof/%Y/%m/%d", blank=True)
    friends = models.ManyToManyField(User, blank=True, related_name="mainfriends")

    def get_friends(self):
        return self.friends.all()

    def get_friends_no(self):
        return self.friends.all().count()

    def __str__(self):
        return str(self.user)


class Gallery(models.Model):
    class Meta:
        db_table = "MainGallery"

    title = models.CharField('Gallery', max_length=200)
    description = models.TextField('Gallery', blank=True)
    image = models.ImageField('Gallery', default="default1.jpg", upload_to="GIMG/%Y/%m/%d")
    demo_link = models.CharField('Gallery', max_length=200, blank=True)
    source_link = models.CharField('Gallery', max_length=200, blank=True)
    vote_total = models.IntegerField('Gallery', default=0, blank=True)
    vote_ratio = models.IntegerField('Gallery', default=0, blank=True)
    created = models.DateTimeField('Gallery', auto_now_add=True)
    autor = models.ForeignKey('Gallery', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class V_Gallery(models.Model):
    class Meta:
        db_table = "MainVGallery"

    title = models.CharField('V_Gallery', max_length=200)
    description = models.TextField('V_Gallery', blank=True)
    video = models.FileField('V_Gallery', default="default.mov", upload_to="GVD/%Y/%m/%d")
    demo_link = models.CharField('V_Gallery', max_length=200, blank=True)
    source_link = models.CharField('V_Gallery', max_length=200, blank=True)
    vote_total = models.IntegerField('V_Gallery', default=0, blank=True)
    vote_ratio = models.IntegerField('V_Gallery', default=0, blank=True)
    created = models.DateTimeField('V_Gallery', auto_now_add=True)
    autor = models.ForeignKey('V_Gallery', on_delete=models.CASCADE, null=True)


class Blog(models.Model):
    class Meta:
        db_table = "MainBlog"

    title = models.CharField('Blog', max_length=255)
    content = models.TextField('Blog', blank=True)
    photo = models.ImageField('Blog', upload_to="blog_photos/%Y/%m/%d/", blank=True)
    time_created = models.DateTimeField('Blog', auto_now_add=True)
    time_update = models.DateTimeField('Blog', auto_now=True)
    autor = models.ForeignKey('Blog', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
