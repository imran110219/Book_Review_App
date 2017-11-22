from django.conf.urls import url
from django.contrib import admin
from .views import(
    book_list,
    book_detail,
)

urlpatterns = [
    # url(r'^$', home, name="home"),
    url(r'^(?P<id>[\w-]+)/$', book_detail, name='detail'),
    url(r'^$', book_list, name='book'),
]