from .models import Book
from Publication.models import Publication
from Author.models import Author
from Category.models import Category
import django_filters
from django import forms


class BookFilter(django_filters.FilterSet):

    bookname = django_filters.CharFilter(field_name='name')
    pagenumber = django_filters.NumberFilter(field_name='no_of_page')

    order = django_filters.OrderingFilter(
        choices=(
            ('name', 'NameASC'),
            ('-name', 'NameDESC'),
            ('no_of_page', 'Page Number ASC'),
            ('-no_of_page', 'Page Number DESC'),

        ),
        fields={
            'name': 'name',
            'name': '-name',
            'no_of_page': 'no_of_page',
            'no_of_page': '-no_of_page',
        },
    )

    publication = django_filters.ModelMultipleChoiceFilter(queryset=Publication.objects.all(), widget=forms.CheckboxSelectMultiple)

    authors = django_filters.ModelMultipleChoiceFilter(queryset=Author.objects.all(), widget=forms.CheckboxSelectMultiple)

    categories = django_filters.ModelMultipleChoiceFilter(queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Book
        fields = ['publication', 'authors', 'categories', ]
        order_by = [
            'name',
            'no_of_page',
        ]
