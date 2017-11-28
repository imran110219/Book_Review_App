from django.db import models
from django.conf import settings
from Book.models import Book

# Create your models here.

class Review(models.Model):
  review_description = models.TextField(max_length=500)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
  book = models.ForeignKey(Book, on_delete=models.CASCADE)

  def __str__(self):
    return self.review_description