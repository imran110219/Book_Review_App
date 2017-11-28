from django.shortcuts import render
from .models import Review

# Create your views here.

def review_list(request):
  if request.user.is_staff or request.user.is_superuser:
    queryset_list = Review.objects.all()

  context = {
    "object_list": queryset_list,
    "title": "List",
  }
  return render(request, "review_list.html", context)