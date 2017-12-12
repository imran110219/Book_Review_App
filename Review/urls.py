from django.conf.urls import url
from django.conf.urls import include, url
from django.contrib import admin
from .views import (
  ReviewUpdate,
)

urlpatterns = [
  # url(r'^reviews/(?P<id>[\w-]+)/$', ReviewUpdate.as_view(), name='review_edit',),
]
