from django.contrib.auth.models import AbstractUser
from django.db import models


class User(models.Model):
    """User model"""
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    email = models.EmailField(blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    middle_name = models.CharField(max_length=50, blank=True)
    first_login = models.DateTimeField(null=True)
    phone = models.CharField(max_length=14, blank=True)
    avatar = models.ImageField(upload_to="prof/%Y/%m/%d", blank=True, null=True)

    def __str__(self):
        return self.username

class FriendRequest(models.Model):
    from_user = models.ForeignKey(User, related_name="from_user", on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name="to_user", on_delete=models.CASCADE)
