from django.contrib import admin
from .models import Publication

# Register your models here.

# class PublicationModelAdmin(admin.ModelAdmin):
#   list_display = ["publication_name"]
#
#   class meta:
#     model = Publication

admin.site.register(Publication)

