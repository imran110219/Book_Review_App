from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from Book.models import Book


# Create your views here.

def book_list(request):
  queryset = Book.objects.all()

  query = request.GET.get("q")

  if query:
    queryset = Book.objects.filter(
      Q(book_name__icontains=query) |
      Q(authors__author_name__icontains=query) |
      Q(categories__category_name__icontains=query) |
      Q(publication__publication_name__icontains=query)
    ).distinct()


  context = {
    "object_list": queryset,
    "title": "Book List",
  }
  return render(request, "book.html", context)


def book_detail(request, id=None):
  instance = get_object_or_404(Book, id=id)

  context = {
    "instance": instance,
  }
  return render(request, "book_details.html", context)


def home(request):
  return render(request, "home.html")
