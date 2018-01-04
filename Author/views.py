from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from Author.models import Author


# Create your views here.

def test_view(request):
  return render(request, "test.html",{})

def author_list(request):
  queryset = Author.objects.all()

  query = request.GET.get("q")

  if query:
    queryset = Author.objects.filter(
      Q(name__icontains=query)
    ).distinct()

  context = {
    "object_list": queryset,
    "title": "Author List",
  }
  return render(request, "author.html", context)


def author_detail(request, id=None):
  instance = get_object_or_404(Author, id=id)

  context = {
    "instance": instance,
  }
  return render(request, "author_books.html", context)
