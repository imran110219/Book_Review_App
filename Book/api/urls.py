from django.conf.urls import url
from django.conf.urls import include, url
from django.contrib import admin
from .views import (
  BookCreateAPIView,
  BookDetailAPIView,
  BookListAPIView,
  BookUpdateAPIView,
  BookDeleteAPIView,
)

urlpatterns = [
  url(r'^$', BookListAPIView.as_view(), name='list'),
  url(r'^create/$', BookCreateAPIView.as_view(), name='create'),
  url(r'^(?P<pk>[\w-]+)/$', BookDetailAPIView.as_view(), name='detail'),
  url(r'^(?P<pk>[\w-]+)/edit/$', BookUpdateAPIView.as_view(), name='update'),
  url(r'^(?P<pk>[\w-]+)/delete/$', BookDeleteAPIView.as_view(), name='delete'),
]
