from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse
from django.db.models import Q
from django.contrib.contenttypes.models import ContentType
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from Book.models import Book
from Review.models import Review
from Comment.models import Comment
from Review.forms import ReviewForm
from Comment.forms import CommentForm


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


@login_required
def home(request):
  return render(request, "home.html")

