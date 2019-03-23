from django.conf.urls import include, url
from django.contrib import admin
from .views import (
  book_list,
  book_detail,
  home
)
app_name = "Book"
urlpatterns = [
  url(r'^$', home, name='home'),
  url(r'^books/$', book_list, name='book'),
  url(r'^books/(?P<id>[\w-]+)/$', book_detail, name='detail'),
  url(r'^books/', include("Review.urls", namespace='reviews')),
]