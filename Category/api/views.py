from rest_framework.generics import (
  CreateAPIView,
  ListAPIView,
  RetrieveAPIView,
  RetrieveUpdateAPIView,
  RetrieveDestroyAPIView
)

from Category.models import Category
from .serializers import CategoryListSerializer, CategoryDetailSerializer, CategoryCreateUpdateSerializer

class CategoryCreateAPIView(CreateAPIView):
  queryset = Category.objects.all()
  serializer_class = CategoryCreateUpdateSerializer

class CategoryListAPIView(ListAPIView):
  queryset = Category.objects.all()
  serializer_class = CategoryListSerializer

class CategoryDetailAPIView(RetrieveAPIView):
  queryset = Category.objects.all()
  serializer_class = CategoryDetailSerializer

class CategoryUpdateAPIView(RetrieveUpdateAPIView):
  queryset = Category.objects.all()
  serializer_class = CategoryCreateUpdateSerializer

class CategoryDeleteAPIView(RetrieveDestroyAPIView):
  queryset = Category.objects.all()
  serializer_class = CategoryDetailSerializer