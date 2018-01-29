from django.conf.urls import url
from django.conf.urls import include, url
from django.contrib import admin
from .views import (
  CategoryCreateAPIView,
  CategoryDetailAPIView,
  CategoryListAPIView,
  CategoryUpdateAPIView,
  CategoryDeleteAPIView,
)
app_name = "Category"
urlpatterns = [
  url(r'^$', CategoryListAPIView.as_view(), name='list'),
  url(r'^create/$', CategoryCreateAPIView.as_view(), name='create'),
  url(r'^(?P<pk>[\w-]+)/$', CategoryDetailAPIView.as_view(), name='detail'),
  url(r'^(?P<pk>[\w-]+)/edit/$', CategoryUpdateAPIView.as_view(), name='update'),
  url(r'^(?P<pk>[\w-]+)/delete/$', CategoryDeleteAPIView.as_view(), name='delete'),
]