from rest_framework import serializers
from ... import models
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class RegistrationSerializer(serializers.ModelSerializer):
    """
    Validate Email and Password and Password1 and Create New User.
    """
    password1 = serializers.CharField(max_length=255, write_only=True)

    class Meta:
        model = models.User
        fields = ["email", "password", "password1"]

    def validate(self, attrs):
        if attrs.get("password") != attrs.get("password1"):
            raise serializers.ValidationError(
                {"detail": "رمز عبور و تکرار آن یکسان نیستند."}
            )
        try:
            validate_password(attrs.get("password"))
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({"password": list(e.messages)})
        return super().validate(attrs)

    def create(self, validated_data):
        validated_data.pop("password1", None)
        return models.User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    """
    ObtainAuthToken have Custom Serializer with (username and password),
     so we customize this and changed to (email and password).
    """

    email = serializers.CharField(label=_("Email"), write_only=True)
    password = serializers.CharField(
        label=_("Password"),
        style={"input_type": "password"},
        trim_whitespace=False,
        write_only=True,
    )
    token = serializers.CharField(label=_("Token"), read_only=True)

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        if email and password:
            user = authenticate(
                request=self.context.get("request"),
                email=email,
                password=password,
            )

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _("Unable to log in with provided credentials.")
                raise serializers.ValidationError(msg, code="authorization")
        else:
            msg = _('Must include "email" and "password".')
            raise serializers.ValidationError(msg, code="authorization")

        attrs["user"] = user
        return attrs


class JWTLoginSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        validated_data = super().validate(attrs)
        validated_data["uid"] = self.user.id
        return validated_data


class MyProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = [
            'id',
            "email",
            "first_name",
            "last_name",
            "image",
            "is_active",
            "is_verified",
            "is_superuser",
            "is_staff",
            "last_login",
            "created_at",
        ]
