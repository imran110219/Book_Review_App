from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import RedirectView
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.db.models import Q
from django.core import serializers
from django.views.generic import TemplateView
from django.utils.html import escape

from .models import Review
from .models import Book
from .models import Profile
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

def profile_review_list(request):
    if request.user.is_staff or request.user.is_superuser:
        profile = get_object_or_404(Profile, user=request.user)
        queryset_list = Review.objects.all().filter(profile=profile)

    context = {
        "object_list": queryset_list,
        "title": "List",
    }
    return render(request, "profile_reviews.html", context)


class ReviewLikeToggle(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        review = get_object_or_404(Review, id=self.kwargs['pk'])
        user = self.request.user
        if user.is_authenticated:
            if user in review.likes.all():
                review.likes.remove(user)
            else:
                review.likes.add(user)
        return reverse("books:detail", args=(review.book.id,))

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
        review = get_object_or_404(Review, id=self.kwargs['pk'])
        return review

    def get_success_url(self, *args, **kwargs):
        review = get_object_or_404(Review, id=self.kwargs['pk'])
        return reverse("books:detail", args=(review.book.id,))


# @login_required
class ReviewDelete(DeleteView):
    model = Review
    template_name = "confirm_delete.html"

    def get_success_url(self, *args, **kwargs):
        review = get_object_or_404(Review, id=self.kwargs['pk'])
        return reverse("books:detail", args=(review.book.id,))

# def save_review_form(request, form, template_name):
#   data = dict()
#   if request.method == 'POST':
#     if form.is_valid():
#       form.save()
#       data['form_is_valid'] = True
#       reviews = Review.objects.all()
#       data['html_book_details'] = render_to_string('book_details.html', {
#         'reviews': reviews
#       })
#     else:
#       data['form_is_valid'] = False
#   context = {'form': form}
#   data['html_form'] = render_to_string(template_name, context, request=request)
#   return JsonResponse(data)
#
#
# def review_list(request):
#   reviews = Review.objects.all()
#   return render(request, 'review_list.html', {'reviews': reviews})
#
#
# def review_create(request):
#   form = ReviewForm()
#   context = {'form': form}
#   html_form = render_to_string('partial_review_create.html',
#                                context,
#                                request=request,
#                                )
#   return JsonResponse({'html_form': html_form})
#
#
# def review_update(request, pk):
#   reviews = Review.objects.get(pk=pk)
#   context = {'reviews': reviews}
#   return render(request, 'review_edit.html', context)
#
#   # def review_delete(request, id):
#   #   review = Review.objects.get(id=id)
#   #   book_id = review.book.id
#   #   review.delete()
#   #   return HttpResponseRedirect('/books/')
#
#
# def review_delete(request, pk):
#   review = get_object_or_404(Review, pk=pk)
#   data = dict()
#   if request.method == 'POST':
#     review.delete()
#     data['form_is_valid'] = True  # This is just to play along with the existing code
#     reviews = Review.objects.all()
#     data['html_book_details'] = render_to_string('book_details.html', {
#       'reviews': reviews
#     })
#   else:
#     context = {'review': review}
#     data['html_form'] = render_to_string('partial_review_delete.html',
#                                          context,
#                                          request=request,
#                                          )
#
#   return JsonResponse(data)
