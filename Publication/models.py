from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Publication(models.Model):
    publication_name = models.CharField(max_length=100)
    publication_description = models.TextField(max_length=500)
    publication_image = models.ImageField(height_field="height_field", width_field="width_field")
    height_field = models.IntegerField(default=255)
    width_field = models.IntegerField(default=255)

    def __unicode__(self):
        return str(self.publication_name)

    def __str__(self):
        return str(self.publication_name)

    def get_absolute_url(self):
        return reverse("publications:detail", kwargs={"id": self.id})
