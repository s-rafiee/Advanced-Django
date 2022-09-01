from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

# from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path(
        "accounts/register/",
        views.RegistrationAPIView.as_view(),
        name="api_registration",
    ),
    path(
        "accounts/login/",
        views.LoginTokenView.as_view(),
        name="api_token_login",
    ),  # Login with token
    path(
        "accounts/logout/",
        views.LogoutTokenView.as_view(),
        name="api_token_logout",
    ),  # Login with token
    # JWT =>
    path(
        "accounts/jwt/create/",
        TokenObtainPairView.as_view(),
        name="jwt_create",
    ),
    path(
        "accounts/jwt/refresh/",
        TokenRefreshView.as_view(),
        name="jwt_refresh",
    ),
    path(
        "accounts/jwt/verify/", TokenVerifyView.as_view(), name="jwt_verify"
    ),
    # Custom JWT
    path(
        "accounts/jwt2/create/",
        views.CreateJWTTokenView.as_view(),
        name="jwt2_create",
    ),
    path(
        "accounts/jwt/profile/",
        views.ProfileJWTView.as_view(),
        name="jwt_profile",
    ),
]
