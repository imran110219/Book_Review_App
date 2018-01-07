from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=11)
    address = models.CharField(max_length=30, blank=True)
    image = models.ImageField(height_field="height_field", width_field="width_field")
    height_field = models.IntegerField(default=255)
    width_field = models.IntegerField(default=255)
    fb_link = models.CharField(max_length=100, blank=True)
    website = models.CharField(max_length=100, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
