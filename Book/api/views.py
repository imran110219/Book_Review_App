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
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly
)

class BookCreateAPIView(CreateAPIView):
  queryset = Book.objects.all()
  serializer_class = BookCreateUpdateSerializer

class BookListAPIView(ListAPIView):
  queryset = Book.objects.all()
  serializer_class = BookListSerializer
  permission_classes = [AllowAny]

class BookDetailAPIView(RetrieveAPIView):
  queryset = Book.objects.all()
  serializer_class = BookDetailSerializer

class BookUpdateAPIView(RetrieveUpdateAPIView):
  permission_classes = [AllowAny,]
  queryset = Book.objects.all()
  serializer_class = BookCreateUpdateSerializer

class BookDeleteAPIView(DestroyAPIView):
  queryset = Book.objects.all()
  serializer_class = BookDetailSerializer

