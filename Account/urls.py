from django.conf.urls import include, url
from django.contrib import admin
from .views import (
  home,
  settings,
  password,
)
app_name = "Book"
urlpatterns = [
  url(r'^$', home, name="home"),
  url(r'^settings/$', settings, name='settings'),
  url(r'^settings/password/$', password, name='password'),
]