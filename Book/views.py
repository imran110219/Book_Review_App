from django.shortcuts import render, get_object_or_404

from Book.models import Book

# Create your views here.

def book_list(request):
  queryset = Book.objects.all()

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

