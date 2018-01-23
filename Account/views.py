from django.contrib.auth import (
  authenticate,
  get_user_model,
  login,
  logout,
)
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .forms import UserLoginForm, UserRegisterForm, UserForm, ProfileForm
from .models import Profile
from django.contrib import messages


def login_view(request):
  print(request.user.is_authenticated)
  next = request.GET.get('next')
  title = "Login"
  form = UserLoginForm(request.POST or None)
  if form.is_valid():
    username = form.cleaned_data.get("username")
    password = form.cleaned_data.get("password")
    user = authenticate(username=username, password=password)
    login(request, user)
    if next:
      return redirect(next)
    return redirect("/books/")
  return render(request, "form.html", {"form": form, "title": title})


def register_view(request):
  print(request.user.is_authenticated())
  next = request.GET.get('next')
  title = "Register"
  form = UserRegisterForm(request.POST or None)
  if form.is_valid():
    user = form.save(commit=False)
    password = form.cleaned_data.get('password1')
    user.set_password(password)
    user.save()

    new_user = authenticate(username=user.username, password=password)
    login(request, new_user)
    if next:
      return redirect(next)
    return redirect("/")

  context = {
    "form": form,
    "title": title
  }
  return render(request, "form.html", context)


def logout_view(request):
  logout(request)
  return redirect("/books/")


@login_required
@transaction.atomic
def update_profile(request):
  title = "Update"
  try:
    profile = request.user.profile
  except ObjectDoesNotExist:
    profile = Profile(user=request.user)
  if request.method == 'POST':
    user_form = UserForm(request.POST, instance=request.user)
    profile_form = ProfileForm(request.POST, instance=profile)
    if user_form.is_valid() and profile_form.is_valid():
      user_form.save()
      profile_form.save()
      messages.success(request, 'Your profile was successfully updated!')
      return redirect('books:home')
    else:
      messages.error(request, 'Please correct the error below.')
  else:
    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance=profile)

  context = {
    'user_form': user_form,
    'profile_form': profile_form,
    "title": title
  }
  return render(request, 'profile.html', context)
