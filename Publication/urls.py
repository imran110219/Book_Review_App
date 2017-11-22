from django.conf.urls import url
from django.contrib import admin
from .views import(
    publication_list,
    publication_detail,
)

urlpatterns = [
    # url(r'^$', home, name="home"),
    url(r'^(?P<id>[\w-]+)/$', publication_detail, name='detail'),
    url(r'^$', publication_list, name='publication'),
]