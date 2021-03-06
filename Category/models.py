from __future__ import unicode_literals

from django.contrib.contenttypes.models import ContentType

from django.db import models
# from django.core.urlresolvers import reverse
from django.urls import reverse


# Create your models here.

class Category(models.Model):
  name = models.CharField(max_length=100)
  image = models.ImageField(height_field="height_field", width_field="width_field")
  height_field = models.IntegerField(default=255)
  width_field = models.IntegerField(default=255)


  def __unicode__(self):
    return str(self.name)


  def __str__(self):
    return str(self.name)


  def get_absolute_url(self):
    return reverse("categories:detail", kwargs={"id": self.id})
