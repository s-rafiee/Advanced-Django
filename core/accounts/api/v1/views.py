from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from ... import models
from rest_framework_simplejwt.views import TokenObtainPairView
from django.shortcuts import get_object_or_404


class RegistrationAPIView(GenericAPIView):
    """
    get email and password in a Post Request type and create new user.
    """
    serializer_class = serializers.RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "email": serializer.validated_data["email"],
                'detail': 'حساب کاربری ایجاد شد.'
            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(TokenObtainPairView):
    """
    Rewrite to create custom post function and using custom serializer.
    """

    serializer_class = serializers.JWTLoginSerializer


class MpProfileView(RetrieveAPIView):
    serializer_class = serializers.MyProfileSerializer
    queryset = models.User.objects.all()
    permission_classes = [IsAuthenticated]

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, id=self.request.user.id)
        return obj
