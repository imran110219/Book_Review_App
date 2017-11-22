from django.shortcuts import render, get_object_or_404

from Category.models import Category


# Create your views here.

def category_list(request):
  queryset = Category.objects.all()

  context = {
    "object_list": queryset,
    "title": "List",
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
