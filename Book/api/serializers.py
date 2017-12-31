from rest_framework.serializers import ModelSerializer

from Book.models import Book

class BookCreateUpdateSerializer(ModelSerializer):
  class Meta:
    model = Book
    fields = [
      'book_name',
      'book_description',
      'publication',
      'authors',
      'categories',
    ]

class BookListSerializer(ModelSerializer):
  class Meta:
    model = Book
    fields = [
      'id',
      'book_name',
      'book_description',
      'publication',
      'authors',
      'categories',
    ]

class BookDetailSerializer(ModelSerializer):
  class Meta:
    model = Book
    fields = [
      'id',
      'book_name',
      'book_description',
      'publication',
      'authors',
      'categories',
    ]