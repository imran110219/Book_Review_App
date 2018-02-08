from django.db import models
# from django.core.urlresolvers import reverse
from django.urls import reverse


# Create your models here.

class Author(models.Model):
  name = models.CharField(max_length=100)
  biography = models.TextField(max_length=500)
  image = models.ImageField(height_field="height_field", width_field="width_field")
  height_field = models.IntegerField(default=255)
  width_field = models.IntegerField(default=255)

  def __unicode__(self):
    return str(self.name)

  def __str__(self):
    return str(self.name)

  def get_absolute_url(self):
    return reverse("authors:detail", kwargs={"id": self.id})

  def get_name(self):
    return self.name