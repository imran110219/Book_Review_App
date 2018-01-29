from django.db import models
# from django.core.urlresolvers import reverse
from django.urls import reverse

# Create your models here.

class Publication(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    logo = models.ImageField(height_field="height_field", width_field="width_field")
    height_field = models.IntegerField(default=255)
    width_field = models.IntegerField(default=255)
    address = models.CharField(max_length=80)
    phone = models.CharField(max_length=11)
    proprietor = models.CharField(max_length=100)
    discount_range = models.FloatField(default=0.0)

    def __unicode__(self):
        return str(self.name)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("publications:detail", kwargs={"id": self.id})
