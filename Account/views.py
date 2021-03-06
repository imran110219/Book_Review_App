from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.core import serializers
from django.contrib.auth.models import User
from Book.models import Book
from Book.filters import BookFilter
from django.contrib.auth.decorators import login_required
from django.db import transaction
from .forms import UserLoginForm, UserRegisterForm, UserForm, ProfileForm
from .models import Profile, UserBook
from django.contrib import messages
import json
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from social_django.models import UserSocialAuth


# def login_view(request):
#     print(request.user.is_authenticated)
#     next = request.GET.get('next')
#     title = "Login"
#     form = UserLoginForm(request.POST or None)
#     if form.is_valid():
#         username = form.cleaned_data.get("username")
#         password = form.cleaned_data.get("password")
#         user = authenticate(username=username, password=password)
#         login(request, user)
#         if next:
#             return redirect(next)
#         return redirect("/books/")
#     return render(request, "form.html", {"form": form, "title": title})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                # return HttpResponseRedirect(reverse('books:home'))
                return HttpResponse(json.dumps({"message": "success"}), content_type="application/json")
            else:
                return HttpResponse(json.dumps({"message": "inactive"}), content_type="application/json")
        else:
            return HttpResponse(json.dumps({"message": "invalid"}), content_type="application/json")
    else:
        return render(request, 'register.html', {})


# def register_view(request):
#     # print(request.user.is_authenticated())
#     next = request.GET.get('next')
#     title = "Register"
#     form = UserRegisterForm(request.POST or None)
#     if form.is_valid():
#         user = form.save(commit=False)
#         password = form.cleaned_data.get('password1')
#         user.set_password(password)
#         user.save()
#
#         new_user = authenticate(username=user.username, password=password)
#         login(request, new_user)
#         if next:
#             return redirect(next)
#         return redirect("/")
#
#     context = {
#         "form": form,
#         "title": title
#     }
    # return render(request, "form.html", context)

def register_view(request):
    if request.method == 'POST':
        register_user_name = request.POST.get('register_user_name')
        register_email_address = request.POST.get('register_email_address')
        register_password = request.POST.get('register_password')
        register_confirm_password = request.POST.get('register_confirm_password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        occupation = request.POST.get('occupation')
        mobile_number = request.POST.get('mobile_number')

        user, created = User.objects.get_or_create(username=register_user_name, email=register_email_address)
        if created:
            user.first_name = first_name
            user.last_name = last_name
            user.set_password(register_password)
            user.save()

            new_user = authenticate(username=register_user_name, password=register_password)
            login(request, new_user)
            return HttpResponse(json.dumps({"message": "success"}), content_type="application/json")
        else:
            return HttpResponse(json.dumps({"message": "duplicate"}), content_type="application/json")

    else:
        return render(request, 'register.html', {})

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
    return render(request, 'profile_edit.html', context)


@login_required
def home(request):
    return render(request, "home.html")


@login_required
def profile(request, username):
    user = get_object_or_404(User, id=request.user.id)
    profile = get_object_or_404(Profile, user=user) #Profile.objects.filter(user=user)
    context = {
        'user': user,
        'profile': profile,
        'title' : 'Profile'
    }
    return render(request, "profile.html", context)

@login_required
def user_books(request, status):
    user = get_object_or_404(User, id=request.user.id)
    profile = get_object_or_404(Profile, user=user) #Profile.objects.filter(user=user)
    flag = 0
    if status == 'wishlist':
        flag = 1
    elif status == 'reading':
        flag = 2
    elif status == 'read':
        flag = 3
    else:
        flag = 4
    user_book = UserBook.objects.filter(user=profile).filter(status=flag).values('id','book','book__name','book__no_of_page','status')
    user_book_list = list(user_book)

    return JsonResponse(user_book_list,  safe=False)


@login_required
def settings(request):
    user = request.user

    try:
        google_login = user.social_auth.get(provider='google-oauth2')
    except UserSocialAuth.DoesNotExist:
        google_login = None

    try:
        github_login = user.social_auth.get(provider='github')
    except UserSocialAuth.DoesNotExist:
        github_login = None

    try:
        twitter_login = user.social_auth.get(provider='twitter')
    except UserSocialAuth.DoesNotExist:
        twitter_login = None

    try:
        facebook_login = user.social_auth.get(provider='facebook')
    except UserSocialAuth.DoesNotExist:
        facebook_login = None

    can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

    return render(request, 'settings.html', {
        'google_login': google_login,
        'github_login': github_login,
        'twitter_login': twitter_login,
        'facebook_login': facebook_login,
        'can_disconnect': can_disconnect
    })


@login_required
def password(request):
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm

    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile-edit')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordForm(request.user)
    return render(request, 'password.html', {'form': form})


# Test View

def test_view(request):
    # book_list = Book.objects.all()
    # book_filter = BookFilter(request.GET, queryset=book_list)
    # temp = book_filter.form
    return render(request, 'test.html') # , {'filter': book_filter})

def test_json(request):
    books = Book.objects.all().values('name')
    booklist = list(books)
    return JsonResponse(booklist,  safe=False)
    # json = serializers.serialize('json', booklist)
    # return HttpResponse(json, content_type='application/json')
