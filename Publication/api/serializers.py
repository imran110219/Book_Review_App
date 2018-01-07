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
      'name',
      'description',
      'address',
      'phone',
      'proprietor',
      'discount_range'
    ]

class PublicationListSerializer(ModelSerializer):
  url = publication_detail_url
  class Meta:
    model = Publication
    fields = [
      'url',
      'id',
      'name',
    ]

class PublicationDetailSerializer(ModelSerializer):
  logo = SerializerMethodField()
  class Meta:
    model = Publication
    fields = [
      'id',
      'name',
      'logo',
      'description',
      'address',
      'phone',
      'proprietor',
      'discount_range'
    ]

  def get_logo(self, obj):
      try:
        logo =obj.logo.url
      except:
        logo = None
      return logo