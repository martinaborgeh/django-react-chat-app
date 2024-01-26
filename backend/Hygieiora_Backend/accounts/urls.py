from django.urls import path

from .views import *
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path("", api_root),
    path("register/", RegisterUserView.as_view(), name="auth-register"),
    path("login/", MyObtainTokenPairView.as_view(), name="token_obtain_pair"),
    path("login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("users/", UsersList.as_view(), name="user-list"),
    path("users/<uuid:pk>/", UserDetail.as_view(), name="user-detail"),
]
