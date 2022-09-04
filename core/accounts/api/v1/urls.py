from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)

# from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path(
        "register/", views.RegistrationAPIView.as_view(), name="api_registration",
    ),
    path(
        "login/", views.LoginView.as_view(), name="login",
    ),
    path(
        "profile/", views.MpProfileView.as_view(), name="my_profile",
    ),
    path(
        "token/verify/", TokenVerifyView.as_view(), name="token_verify"
    ),
    path(
        "token/refresh/", TokenRefreshView.as_view(), name="token_refresh"
    )
]
