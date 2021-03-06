from django.conf.urls import url
from django.contrib import admin
from .views import(
    author_list,
    author_detail
)
app_name = "Author"
urlpatterns = [
    # url(r'^$', home, name="home"),
    url(r'^$', author_list, name="author"),
    url(r'^(?P<id>[\w-]+)/$', author_detail, name='detail'),
]
