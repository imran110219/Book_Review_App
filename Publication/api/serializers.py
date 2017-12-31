from rest_framework.serializers import (
  ModelSerializer,
  SerializerMethodField,
  HyperlinkedIdentityField,
)

from Publication.models import Publication

publication_detail_url = HyperlinkedIdentityField(
        view_name='publications-api:detail'
    )

class PublicationCreateUpdateSerializer(ModelSerializer):
  class Meta:
    model = Publication
    fields = [
      'publication_name',
      'publication_description',
    ]

class PublicationListSerializer(ModelSerializer):
  url = publication_detail_url
  class Meta:
    model = Publication
    fields = [
      'url',
      'id',
      'publication_name',
    ]

class PublicationDetailSerializer(ModelSerializer):
  publication_image = SerializerMethodField()
  class Meta:
    model = Publication
    fields = [
      'id',
      'publication_name',
      'publication_description',
      'publication_image'
    ]

  def get_publication_image(self, obj):
      try:
        publication_image =obj.publication_image.url
      except:
        publication_image = None
      return publication_image