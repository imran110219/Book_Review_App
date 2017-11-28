from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse
from django.db.models import Q
from django.contrib.contenttypes.models import ContentType

from Book.models import Book
from Review.models import Review
from Review.forms import ReviewForm


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

  if request.method == 'POST':
    review_form = ReviewForm(data=request.POST)
    if review_form.is_valid():
      new_review = review_form.save(commit=False)
      # Assign the current post to the comment
      new_review.book = book
      # Save the comment to the database
      new_review.save()

    return HttpResponseRedirect('/book/', args=[book.id])


  else:
    review_form = ReviewForm()
    context = {
      'user': request.user,
      'book': book,
      'reviews': reviews,
      'review_form': review_form
    }

    return render(request, 'book_details.html', context)


def home(request):
  return render(request, "home.html")
