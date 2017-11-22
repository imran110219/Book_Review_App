from django.shortcuts import render, get_object_or_404

from Author.models import Author


# Create your views here.

def test_view(request):
  return render(request, "test.html",{})

def author_list(request):
  queryset = Author.objects.all()

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
