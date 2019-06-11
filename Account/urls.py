from django.conf.urls import include, url
from django.contrib import admin
from .views import (
    home,
    profile,
    update_profile,
    settings,
    password,
)

app_name = "Account"

urlpatterns = [
    url(r'^profile/(?P<username>[\w.@+-]+)/$', profile, name="profile"),
    url(r'^profile/edit/$', update_profile, name="profile-edit"),
    url(r'^settings/$', settings, name='settings'),
    url(r'^settings/password/$', password, name='password'),
]
