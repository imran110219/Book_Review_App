from rest_framework.generics import (
  CreateAPIView,
  ListAPIView,
  RetrieveAPIView,
  RetrieveUpdateAPIView,
  DestroyAPIView
)

from Book.models import Book
from .serializers import (
  BookListSerializer,
  BookDetailSerializer,
  BookCreateUpdateSerializer,
)

class BookCreateAPIView(CreateAPIView):
  queryset = Book.objects.all()
  serializer_class = BookCreateUpdateSerializer

class BookListAPIView(ListAPIView):
  queryset = Book.objects.all()
  serializer_class = BookListSerializer

class BookDetailAPIView(RetrieveAPIView):
  queryset = Book.objects.all()
  serializer_class = BookDetailSerializer

class BookUpdateAPIView(RetrieveUpdateAPIView):
  queryset = Book.objects.all()
  serializer_class = BookCreateUpdateSerializer

class BookDeleteAPIView(DestroyAPIView):
  queryset = Book.objects.all()
  serializer_class = BookDetailSerializer

