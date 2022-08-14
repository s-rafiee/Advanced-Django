from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff=False, is_superuser=False, is_active=False, is_verified=False,
                     **extra_fields):
        if not email:
            raise ValueError('Email is Required.')

        user = self.model(
            email=email,
            password=password,
            is_staff=is_staff,
            is_active=is_active,
            is_verified=is_verified,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password=password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        return self._create_user(email, password=password, is_staff=True, is_superuser=True, is_active=True,
                                 is_verified=True, **extra_fields)
