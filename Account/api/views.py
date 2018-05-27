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
from .serializers import UserListSerializer, UserDetailSerializer, UserCreateUpdateSerializer


class UserCreateAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    queryset = Profile.objects.all()
    serializer_class = UserCreateUpdateSerializer
    # def post(self, request, *args, **kwargs):
    #   return self.create(request, *args, **kwargs)

class UserListAPIView(ListAPIView):
    # permission_classes = (IsAuthenticated,)
    permission_classes = [AllowAny]
    queryset = Profile.objects.all()
    serializer_class = UserListSerializer


class UserDetailAPIView(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = UserDetailSerializer


class UserUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = UserCreateUpdateSerializer


class UserDeleteAPIView(RetrieveDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = UserDetailSerializer
