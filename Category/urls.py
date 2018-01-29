from django.conf.urls import url
from django.contrib import admin
from .views import(
    category_list,
    category_detail,
)
app_name = "Category"
urlpatterns = [
    # url(r'^$', home, name="home"),
    url(r'^(?P<id>[\w-]+)/$', category_detail, name='detail'),
    url(r'^$', category_list, name='category'),
]