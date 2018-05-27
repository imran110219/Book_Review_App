from django.conf.urls import url
from django.conf.urls import include, url
from django.contrib import admin
from .views import (
  UserCreateAPIView,
  UserDetailAPIView,
  UserListAPIView,
  UserUpdateAPIView,
  UserDeleteAPIView,
)
app_name = "Author"
urlpatterns = [
  url(r'^$', UserListAPIView.as_view(), name='list'),
  url(r'^create/$', UserCreateAPIView.as_view(), name='create'),
  url(r'^(?P<pk>[\w-]+)/$', UserDetailAPIView.as_view(), name='detail'),
  url(r'^(?P<pk>[\w-]+)/edit/$', UserUpdateAPIView.as_view(), name='update'),
  url(r'^(?P<pk>[\w-]+)/delete/$', UserDeleteAPIView.as_view(), name='delete'),
]