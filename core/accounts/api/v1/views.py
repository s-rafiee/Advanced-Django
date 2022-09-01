from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from ... import models
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from django.shortcuts import get_object_or_404


class RegistrationAPIView(GenericAPIView):
    serializer_class = serializers.RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {"email": serializer.validated_data["email"]}
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginTokenView(ObtainAuthToken):
    """
    for create custom login, we overwrite ObtainAuthToken Class, by default we can call this class in url.
    customized Class has customized Serializer (LoginSerializer).
    """

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )

        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {
                "token": token.key,
                "user_id": user.pk,
                "email": user.email,
            }
        )


class LogoutTokenView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CreateJWTTokenView(TokenObtainPairView):
    """
    Rewrite to create custom post function and using custom serializer.
    """

    serializer_class = serializers.JWTCreateTokenSerializer


class ProfileJWTView(RetrieveAPIView):
    serializer_class = serializers.ProfileSerializer
    queryset = models.User.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user)
        return "obj"
