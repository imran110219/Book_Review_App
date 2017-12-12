from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Review
from .models import Book
from .forms import ReviewForm


# Create your views here.

def review_list(request):
  if request.user.is_staff or request.user.is_superuser:
    queryset_list = Review.objects.all()

  context = {
    "object_list": queryset_list,
    "title": "List",
  }
  return render(request, "review_list.html", context)

# @login_required #(login_url='/login/') #LOGIN_URL = '/login/'
# def review_delete(request, id):
#     # obj = get_object_or_404(Comment, id=id)
#     # obj = Comment.objects.get(id=id)
#     try:
#         obj = Review.objects.get(id=id)
#         book = Book.objects.filter(review=obj)
#     except:
#         raise Http404
#
#     if obj.user != request.user:
#         # messages.success(request, "You do not have permission to view this.")
#         # Http404
#         response = HttpResponse("You do not have permission to delete this.")
#         response.status_code =403
#         return response
#         # return render(request, "confirm_delete.html", context, status_code=403)
#
#     if request.method == "POST":
#         obj.delete()
#         messages.success(request, "This has been deleted.")
#         return HttpResponseRedirect('/books/' + str(book.id))
#     context = {
#         "object": obj
#     }
#     return render(request, "confirm_delete.html", context)

# @login_required
class ReviewUpdate(UpdateView):  # Note that we are using UpdateView and not FormView
  model = Review
  # fields = ('review_description',)
  form_class = ReviewForm
  template_name = "review_edit.html"

  def get_object(self, *args, **kwargs):
    review = get_object_or_404(Review, id=self.kwargs['id'])
    return review

  def get_success_url(self, *args, **kwargs):
    review = get_object_or_404(Review, id=self.kwargs['id'])
    return reverse("books:detail", args = (review.book.id,))

# @login_required
class ReviewDelete(DeleteView):
  model = Review
  template_name = "confirm_delete.html"

  def get_success_url(self, *args, **kwargs):
    review = get_object_or_404(Review, pk=self.kwargs['pk'])
    return reverse("books:detail", args = (review.book.id,))
