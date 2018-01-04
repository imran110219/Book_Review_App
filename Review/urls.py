from django.conf.urls import url
from django.conf.urls import include, url
from django.contrib import admin
from .views import (
  ReviewUpdate,
  ReviewDelete,
)

urlpatterns = [
  url(r'^reviews/(?P<pk>\d+)/edit/$', ReviewUpdate.as_view(), name='review_update'),
  url(r'^reviews/(?P<pk>\d+)/delete/$', ReviewDelete.as_view(), name='review_delete'),
]
