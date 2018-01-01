from django.db import models
from django.conf import settings
from Book.models import Book
from django.core.urlresolvers import reverse

# Create your models here.

class Review(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField(max_length=500)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
  book = models.ForeignKey(Book, on_delete=models.CASCADE)
  updated = models.DateTimeField(auto_now=True, auto_now_add=False)
  timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

  def __str__(self):
    return self.description

  # def get_absolute_url(self):
  #   return reverse("reviews:details", kwargs={"id": self.id})