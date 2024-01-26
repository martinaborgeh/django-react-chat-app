from django.contrib.auth import logout

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import CustomUser
from .serializers import *
from .permissions import IsOwnerOrReadOnly


@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "users": reverse("user-list", request=request, format=format),
        }
    )


class RegisterUserView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterUserSerializer


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class UserLogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)


class UsersList(generics.ListCreateAPIView):
    """
    List all users, or create a new User.
    """

    queryset = CustomUser.objects.all()
    permission_classes = (IsAdminUser,)
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a user instance.
    """

    queryset = CustomUser.objects.all()
    permission_classes = (IsAdminUser, IsOwnerOrReadOnly)
    serializer_class = UserSerializer
