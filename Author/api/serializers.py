from rest_framework.serializers import (
  ModelSerializer,
  SerializerMethodField,
  HyperlinkedIdentityField,
)

from Author.models import Author

author_detail_url = HyperlinkedIdentityField(
        view_name='authors-api:detail'
    )

class AuthorCreateUpdateSerializer(ModelSerializer):
  class Meta:
    model = Author
    fields = [
      'name',
      'biography',
    ]

class AuthorListSerializer(ModelSerializer):
  url = author_detail_url
  class Meta:
    model = Author
    fields = [
      'url',
      'id',
      'name',
    ]

class AuthorDetailSerializer(ModelSerializer):
  image = SerializerMethodField()
  class Meta:
    model = Author
    fields = [
      'id',
      'name',
      'image',
      'biography',
    ]

  def get_image(self, obj):
      try:
        image =obj.image.url
      except:
        image = None
      return image