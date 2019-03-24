from django.shortcuts import render, get_object_or_404

from Publication.models import Publication

# Create your views here.

def publication_list(request):
  queryset = Publication.objects.all()

  context = {
    "object_list": queryset,
    "title": "Publications",
  }
  return render(request, "publication.html", context)

def publication_detail(request, id=None):
  instance = get_object_or_404(Publication, pk=id)

  context = {
    "instance": instance,
  }
  return render(request, "publication_books.html", context)