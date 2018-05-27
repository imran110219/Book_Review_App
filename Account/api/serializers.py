from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    HyperlinkedIdentityField,
)

from django.contrib.auth.models import User
from Account.models import Profile

user_detail_url = HyperlinkedIdentityField(
    view_name='users-api:detail'
)

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class UserProfileCreateUpdateSerializer(ModelSerializer):
    user = UserSerializer(required=True)
    image = SerializerMethodField()

    class Meta:
        model = Profile
        fields = [
            'user',
            'user_role',
            'phone',
            'address',
            'image',
            'fb_link',
            'website',
        ]

    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image


class UserProfileListSerializer(ModelSerializer):
    user = UserSerializer(required=True)
    url = user_detail_url

    class Meta:
        model = Profile
        fields = [
            'url',
            'id',
            'user',
        ]


class UserProfileDetailSerializer(ModelSerializer):
    user = UserSerializer(required=True)
    image = SerializerMethodField()

    class Meta:
        model = Profile
        fields = [
            'id',
            'user',
            'user_role',
            'phone',
            'address',
            'image',
            'fb_link',
            'website',
        ]

    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image
