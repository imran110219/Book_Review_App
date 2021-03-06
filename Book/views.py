from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse, render_to_response, HttpResponse
from django.db.models import Q
from django.contrib.contenttypes.models import ContentType
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse

from .models import Book
from .filters import BookFilter
from Author.models import Author
from Category.models import Category
from Publication.models import Publication
from Review.models import Review
from Comment.models import Comment
from Review.forms import ReviewForm
from Comment.forms import CommentForm


# Create your views here.

def book_list(request):

    booklist = Book.objects.all()

    # if request.method == "POST":
    #     filters = json.loads(request.body)
    #
    #     if filters['categories']:
    #         booklist = booklist.filter(categories__id__in=list(map(int, filters['categories'])))
    #     if filters['authors']:
    #         booklist = booklist.filter(authors__id__in=list(map(int, filters['authors'])))
    #     if filters['publications']:
    #         booklist = booklist.filter(publications__id__in=list(map(int, filters['publications'])))


    authorlist = Author.objects.all()
    categorylist = Category.objects.all()
    publicationlist = Publication.objects.all()

    # query = request.GET.get("q")
    #
    # if query:
    #     queryset = Book.objects.filter(
    #         Q(name__icontains=query) |
    #         Q(authors__author_name__icontains=query) |
    #         Q(categories__category_name__icontains=query) |
    #         Q(publication__publication_name__icontains=query)
    #     ).distinct()

    context = {
        "booklist": booklist,
        "categorylist": categorylist,
        "publicationlist": publicationlist,
        "authorlist": authorlist,
        # "filter": book_filter,
        "title": "Books",
    }

    return render(request, "book.html", context)

def filter_book_list(request):

    booklist = Book.objects.all()

    if request.method == "POST":
        filters = json.loads(request.body)

        if filters['categories']:
            booklist = booklist.filter(categories__id__in=list(map(int, filters['categories'])))
        if filters['authors']:
            booklist = booklist.filter(authors__id__in=list(map(int, filters['authors'])))
        if filters['publications']:
            booklist = booklist.filter(publication__id__in=list(map(int, filters['publications'])))

        if filters['sort_by'] == 'name':
            if filters['sort_order'] == 'asc':
                booklist = booklist.order_by('name')
            else:
                booklist = booklist.order_by('-name')


    books = booklist.values('id','name','image','ratings')

    booklistjs = list(books)

    return JsonResponse(booklistjs, safe=False)
    # return booklist

def book_detail(request, id=None):
    book = get_object_or_404(Book, id=id)
    reviews = Review.objects.filter(book=book)
    comments = Comment.objects.all()  # filter(review=reviews)

    review_form = ReviewForm()
    comment_form = CommentForm()
    if request.method == 'POST' and request.user.is_authenticated:
        review_form = ReviewForm(data=request.POST)
        comment_form = CommentForm(data=request.POST)
        if review_form.is_valid():
            new_review = review_form.save(commit=False)
            new_review.book = book
            new_review.user = request.user
            new_review.save()

        else:
            new_comment = comment_form.save(commit=False)
            # new_comment.review = Review.objects.filter(id=request.POST.review)
            new_comment.user = request.user
            new_comment.save()

        return HttpResponseRedirect('/books/' + str(book.id))

    context = {
        'user': request.user,
        'book': book,
        'reviews': reviews,
        'review_form': review_form,
        'comments': comments,
        'comment_form': comment_form,
    }

    return render(request, 'book_details.html', context)


# Render Hompage
def home(request):
    context = {
        "title": "Home"
    }
    return render(request, "home.html", context)


def book_search(request):
    print(request.POST['search_text'])
    if request.method == "POST":
        search_text = request.POST.get('search_text')
    else:
        search_text = ''

    books = Book.objects.filter(name__icontains=search_text)

    return render_to_response('book_search.html', {'books': books})
