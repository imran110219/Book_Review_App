from __future__ import unicode_literals

from django.contrib.contenttypes.models import ContentType

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __unicode__(self):
        return str(self.category_name)

    def __str__(self):
        return str(self.category_name)

    def get_absolute_url(self):
        return reverse("categories:detail", kwargs={"id": self.id})