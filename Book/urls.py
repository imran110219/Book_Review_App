from django.conf.urls import url
from django.contrib import admin
from .views import (
  book_list,
  book_detail,
  home,
)

urlpatterns = [
  url(r'^$', home, name="home"),
  url(r'^books/(?P<id>[\w-]+)/$', book_detail, name='detail'),
  url(r'^books/$', book_list, name='book'),
]
