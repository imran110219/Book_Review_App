from django.db import models
from django.contrib.auth.models import User
from Book.models import Book
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    USER_TYPE_CHOICES = (
        (1, 'user'),
        (2, 'publisher'),
        (3, 'author'),
        (4, 'moderator'),
        (5, 'admin'),
    )
    user_role = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=1)
    phone = models.CharField(max_length=11, blank=True)
    address = models.CharField(max_length=30, blank=True)
    image = models.ImageField(height_field="height_field", width_field="width_field", blank=True)
    height_field = models.IntegerField(default=255)
    width_field = models.IntegerField(default=255)
    fb_link = models.CharField(max_length=100, blank=True)
    website = models.CharField(max_length=100, blank=True)
    books = models.ManyToManyField(Book, through='UserBook')

    def __str__(self):
        return str(self.user.username)

    def __unicode__(self):
        return str(self.user.username)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

class UserBook(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    STATUS_CHOICES = (
        (1, 'wishlist'),
        (2, 'reading'),
        (3, 'read'),
    )
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=0)

