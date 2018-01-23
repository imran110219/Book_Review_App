from rest_framework.serializers import (
  ModelSerializer,
  SerializerMethodField,
  HyperlinkedIdentityField,
)

from Category.models import Category

author_detail_url = HyperlinkedIdentityField(
        view_name='categories-api:detail'
    )

class CategoryCreateUpdateSerializer(ModelSerializer):
  class Meta:
    model = Category
    fields = [
      'name',
    ]

class CategoryListSerializer(ModelSerializer):
  url = author_detail_url
  class Meta:
    model = Category
    fields = [
      'url',
      'id',
      'name',
    ]

class CategoryDetailSerializer(ModelSerializer):
  image = SerializerMethodField()
  class Meta:
    model = Category
    fields = [
      'id',
      'name',
      'image',
    ]

  def get_image(self, obj):
      try:
        image =obj.image.url
      except:
        image = None
      return image