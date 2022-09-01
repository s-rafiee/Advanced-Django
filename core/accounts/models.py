from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .userManager import UserManager
import jdatetime
import datetime


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom User Model for our app.
    """

    email = models.EmailField(max_length=255, unique=True)
    # The password was defined by default in AbstractBaseUser.
    first_name = models.CharField(max_length=256, null=True)
    last_name = models.CharField(max_length=256, null=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    image = models.ImageField(
        blank=True, null=True, upload_to="users/%Y/%m/%d/"
    )
    last_login = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    # Set Manager
    objects = UserManager()

    def __str__(self):
        """Return string representation of our user"""
        return self.email

    def jlast_login(self):
        return jdatetime.datetime.fromgregorian(
            datetime=self.last_login
        ).strftime("%Y-%m-%d %H:%M:%S")

    def jcreated_at(self):
        return jdatetime.datetime.fromgregorian(
            datetime=self.created_at
        ).strftime("%Y-%m-%d %H:%M:%S")

    def jupdated_at(self):
        return jdatetime.datetime.fromgregorian(
            datetime=self.updated_at
        ).strftime("%Y-%m-%d %H:%M:%S")
