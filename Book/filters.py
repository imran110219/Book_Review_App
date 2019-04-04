from .models import Book
import django_filters

class BookFilter(django_filters.FilterSet):

    publication__name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Book
        fields = ['authors', 'categories', ]