"""bookreview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

from Account.views import (login_view, register_view, logout_view, update_profile)

urlpatterns = [
  url(r'^', include("Book.urls", namespace='books')),
  url(r'api/books/', include("Book.api.urls", namespace='books-api')),
  url(r'^admin/', admin.site.urls),
  url(r'^register/', register_view, name='register'),
  url(r'^update/', update_profile, name='update'),
  url(r'^login/', login_view, name='login'),
  url(r'^logout/', logout_view, name='logout'),
  url(r'^oauth/', include('social_django.urls', namespace='social')),
  url(r'^ratings/', include('star_ratings.urls', namespace='ratings')),
  url(r'^categories/', include("Category.urls", namespace='categories')),
  url(r'api/categories/', include("Category.api.urls", namespace='categories-api')),
  url(r'^authors/', include("Author.urls", namespace='authors')),
  url(r'api/authors/', include("Author.api.urls", namespace='authors-api')),
  url(r'^publications/', include("Publication.urls", namespace='publications')),
  url(r'api/publications/', include("Publication.api.urls", namespace='publications-api')),
  url(r'^api-auth/', include('rest_framework.urls'))
]

if settings.DEBUG:
  urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
