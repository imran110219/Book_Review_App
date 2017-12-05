from django.db import models
from django.conf import settings
from Review.models import Review

# Create your models here.

class Comment(models.Model):
  comments = models.TextField(max_length=500)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
  review = models.ForeignKey(Review, on_delete=models.CASCADE)

  def __str__(self):
    return self.comments

  def review_comment(self):  # replies
    return Comment.objects.filter(review=self)