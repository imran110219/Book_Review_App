from rest_framework.generics import (
  CreateAPIView,
  ListAPIView,
  RetrieveAPIView,
  RetrieveUpdateAPIView,
  RetrieveDestroyAPIView
)

from Author.models import Author
from .serializers import AuthorListSerializer, AuthorDetailSerializer, AuthorCreateUpdateSerializer

class AuthorCreateAPIView(CreateAPIView):
  queryset = Author.objects.all()
  serializer_class = AuthorCreateUpdateSerializer

class AuthorListAPIView(ListAPIView):
  queryset = Author.objects.all()
  serializer_class = AuthorListSerializer

class AuthorDetailAPIView(RetrieveAPIView):
  queryset = Author.objects.all()
  serializer_class = AuthorDetailSerializer

class AuthorUpdateAPIView(RetrieveUpdateAPIView):
  queryset = Author.objects.all()
  serializer_class = AuthorCreateUpdateSerializer

class AuthorDeleteAPIView(RetrieveDestroyAPIView):
  queryset = Author.objects.all()
  serializer_class = AuthorDetailSerializer