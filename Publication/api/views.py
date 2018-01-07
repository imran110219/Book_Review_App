from rest_framework.generics import (
  CreateAPIView,
  ListAPIView,
  RetrieveAPIView,
  RetrieveUpdateAPIView,
  RetrieveDestroyAPIView
)

from Publication.models import Publication
from .serializers import PublicationListSerializer, PublicationDetailSerializer, PublicationCreateUpdateSerializer

class PublicationCreateAPIView(CreateAPIView):
  queryset = Publication.objects.all()
  serializer_class = PublicationCreateUpdateSerializer

class PublicationListAPIView(ListAPIView):
  queryset = Publication.objects.all()
  serializer_class = PublicationListSerializer

class PublicationDetailAPIView(RetrieveAPIView):
  queryset = Publication.objects.all()
  serializer_class = PublicationDetailSerializer

class PublicationUpdateAPIView(RetrieveUpdateAPIView):
  queryset = Publication.objects.all()
  serializer_class = PublicationCreateUpdateSerializer

class PublicationDeleteAPIView(RetrieveDestroyAPIView):
  queryset = Publication.objects.all()
  serializer_class = PublicationDetailSerializer