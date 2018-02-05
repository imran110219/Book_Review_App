from django.conf.urls import include, url
from django.contrib import admin
from .views import (
  book_list,
  book_detail,
)
app_name = "Book"
urlpatterns = [
  url(r'^(?P<id>[\w-]+)/$', book_detail, name='detail'),
  url(r'^$', book_list, name='book'),
  url(r'^', include("Review.urls", namespace='reviews')),
]