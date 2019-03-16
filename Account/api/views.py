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

from Account.models import Profile
from .serializers import UserProfileListSerializer, UserProfileDetailSerializer, UserProfileCreateUpdateSerializer


class UserCreateAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    queryset = Profile.objects.all()
    serializer_class = UserProfileCreateUpdateSerializer
    # def post(self, request, *args, **kwargs):
    #   return self.create(request, *args, **kwargs)

class UserListAPIView(ListAPIView):
    # permission_classes = (IsAuthenticated,)
    permission_classes = [AllowAny]
    queryset = Profile.objects.all()
    serializer_class = UserProfileListSerializer


class UserDetailAPIView(RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Profile.objects.all()
    serializer_class = UserProfileDetailSerializer


class UserUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = [AllowAny]
    queryset = Profile.objects.all()
    serializer_class = UserProfileCreateUpdateSerializer


class UserDeleteAPIView(RetrieveDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = UserProfileDetailSerializer
