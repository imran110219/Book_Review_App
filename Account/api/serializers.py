from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    HyperlinkedIdentityField,
)

from Account.models import Profile

user_detail_url = HyperlinkedIdentityField(
    view_name='users-api:detail'
)


class UserCreateUpdateSerializer(ModelSerializer):
    image = SerializerMethodField()

    class Meta:
        model = Profile
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
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


class UserListSerializer(ModelSerializer):
    url = user_detail_url

    class Meta:
        model = Profile
        fields = [
            'url',
            'id',
            'username',
        ]


class UserDetailSerializer(ModelSerializer):
    image = SerializerMethodField()

    class Meta:
        model = Profile
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
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
