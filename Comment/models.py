from django.db import models
from django.conf import settings
from Review.models import Review

# Create your models here.

class Comment(models.Model):
  comments = models.TextField(max_length=500)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
  review = models.ForeignKey(Review, on_delete=models.CASCADE)
  updated = models.DateTimeField(auto_now=True, auto_now_add=False)
  timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

  def __str__(self):
    return self.comments

  def review_comment(self):  # replies
    return Comment.objects.filter(review=self)