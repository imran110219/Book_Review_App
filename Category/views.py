try:
    from urllib import quote_plus #pthon 2
except:
    pass

try:
    from urllib.parse import quote_plus #pthon 3
except:
    pass

from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from django.shortcuts import render, get_object_or_404

from Category.models import Category


# Create your views here.

def category_list(request):
  queryset = Category.objects.all()

  context = {
    "object_list": queryset,
    "title": "Categories",
  }
  return render(request, "category.html", context)

def category_detail(request, id=None):
  instance = get_object_or_404(Category, id=id)

  context = {
    "instance": instance,
  }
  return render(request, "category_books.html", context)

# def home(request):
#   context = {
#     "title": "Home",
#   }
#   return render(request, "base.html", context)
