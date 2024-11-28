from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User


# class User(models.Model):
#     """User model"""
#     username = models.CharField(max_length=150, unique=True)
#     first_name = models.CharField(max_length=150, blank=True)
#     last_name = models.CharField(max_length=150, blank=True)
#     email = models.EmailField(blank=True)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     middle_name = models.CharField(max_length=50, blank=True)
#     first_login = models.DateTimeField(null=True)
#     phone = models.CharField(max_length=14, blank=True)
#     avatar = models.ImageField(upload_to="prof/%Y/%m/%d", blank=True, null=True)
#     friends = models.ManyToManyField('User', blank=True)
#     def __str__(self):
#         return self.username

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='nameuser')
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    middle_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=14, blank=True)
    avatar = models.ImageField(upload_to="prof/%Y/%m/%d", blank=True, default="default.jpeg")
    friends = models.ManyToManyField(User, blank=True)
    update = models.DateTimeField(auto_now=True)
    create = models.DateTimeField(auto_now_add=True)
    birth_date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    proffecy = models.CharField(max_length=100, blank=True, null=True)
    bg_PIC = models.ImageField(upload_to="prof/%Y/%m/%d", blank=True, default="defbg.jpg")
    status = models.CharField(max_length=250, blank=True, null=True)

    def get_friends(self):
        return self.friends.all()

    def get_friends_no(self):
        return self.friends.all().count()

    def __str__(self):
        return str(self.user)


STATUS_CHOICES = (
    ('send', 'send'),
    ('accepted', 'accepted')
)


class Relationship(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='receiver')
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)
    update = models.DateTimeField(auto_now=True)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender}-{self.receiver}-{self.status}'


class Status(models.Model):
    content = models.TextField(blank=True)

    def __str__(self):
        return str(self.content)
