from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from Author.models import Author


# Create your views here.

def author_list(request):
    queryset = Author.objects.all()

    # page = request.GET.get('page', 1)
    #
    # paginator = Paginator(queryset, 12)
    # try:
    #     queryset = paginator.page(page)
    # except PageNotAnInteger:
    #     queryset = paginator.page(1)
    # except EmptyPage:
    #     queryset = paginator.page(paginator.num_pages)

    query = request.GET.get("q")

    if query:
        queryset = Author.objects.filter(
            Q(name__icontains=query)
        ).distinct()

    context = {
        "object_list": queryset,
        "title": "Authors",
    }
    return render(request, "author.html", context)


def author_detail(request, id=None):
    instance = get_object_or_404(Author, id=id)

    context = {
        "instance": instance,
    }
    return render(request, "author_books.html", context)
