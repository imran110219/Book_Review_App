from .models import Book
from Publication.models import Publication
import django_filters
from django import forms


class BookFilter(django_filters.FilterSet):

    publication = django_filters.ModelMultipleChoiceFilter(queryset=Publication.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Book
        fields = ['publication', 'authors', 'categories', ]