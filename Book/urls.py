from django.conf.urls import include, url
from django.contrib import admin
from .views import (
  home,
  book_search,
  book_list,
  book_detail
)
app_name = "Book"
urlpatterns = [
  url(r'^$', home, name='home'),
  url(r'^books/$', book_list, name='book'),
  url(r'^books/search/$', book_search, name='search'),
  url(r'^books/(?P<id>[\w-]+)/$', book_detail, name='detail'),
  url(r'^books/', include("Review.urls", namespace='reviews')),
]