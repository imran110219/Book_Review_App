from django.conf.urls import url
from django.conf.urls import include, url
from django.contrib import admin
from .views import (
  PublicationCreateAPIView,
  PublicationDetailAPIView,
  PublicationListAPIView,
  PublicationUpdateAPIView,
  PublicationDeleteAPIView,
)

urlpatterns = [
  url(r'^$', PublicationListAPIView.as_view(), name='list'),
  url(r'^create/$', PublicationCreateAPIView.as_view(), name='create'),
  url(r'^(?P<pk>[\w-]+)/$', PublicationDetailAPIView.as_view(), name='detail'),
  url(r'^(?P<pk>[\w-]+)/edit/$', PublicationUpdateAPIView.as_view(), name='update'),
  url(r'^(?P<pk>[\w-]+)/delete/$', PublicationDeleteAPIView.as_view(), name='delete'),
]