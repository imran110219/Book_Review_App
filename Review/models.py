from django.db import models
from django.conf import settings

from Account.models import Profile
from Book.models import Book
# from django.core.urlresolvers import reverse
from django.urls import reverse


# Create your models here.

class Review(models.Model):
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=500)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default=1)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='review_likes')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.description

    # def get_like_url(self):
    #   return reverse("reviews:like-toggle", kwargs={"id": self.id})

    # def get_absolute_url(self):
    #   return reverse("reviews:details", kwargs={"id": self.id})
