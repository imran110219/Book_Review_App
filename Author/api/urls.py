from django.conf.urls import url
from django.conf.urls import include, url
from django.contrib import admin
from .views import (
  AuthorCreateAPIView,
  AuthorDetailAPIView,
  AuthorListAPIView,
  AuthorUpdateAPIView,
  AuthorDeleteAPIView,
)

urlpatterns = [
  url(r'^$', AuthorListAPIView.as_view(), name='list'),
  url(r'^create/$', AuthorCreateAPIView.as_view(), name='create'),
  url(r'^(?P<pk>[\w-]+)/$', AuthorDetailAPIView.as_view(), name='detail'),
  url(r'^(?P<pk>[\w-]+)/edit/$', AuthorUpdateAPIView.as_view(), name='update'),
  url(r'^(?P<pk>[\w-]+)/delete/$', AuthorDeleteAPIView.as_view(), name='delete'),
]