from rest_framework.generics import (
  CreateAPIView,
  ListAPIView,
  RetrieveAPIView,
  RetrieveUpdateAPIView,
  RetrieveDestroyAPIView
)

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly
)


from Author.models import Author
from .serializers import AuthorListSerializer, AuthorDetailSerializer, AuthorCreateUpdateSerializer

class AuthorCreateAPIView(CreateAPIView):
  queryset = Author.objects.all()
  serializer_class = AuthorCreateUpdateSerializer

  # def post(self, request, *args, **kwargs):
  #   return self.create(request, *args, **kwargs)

class AuthorListAPIView(ListAPIView):
  # permission_classes = (IsAuthenticated,)
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