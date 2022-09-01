from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordResetForm,
    SetPasswordForm,
)


class UserLoginForm(AuthenticationForm):
    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    username = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control text-center",
                "type": "email",
                "placeholder": "ایمیل",
                "autofocus": "autofocus",
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control text-center",
                "placeholder": "رمز عبور",
            }
        )
    )


class PasswordReset(PasswordResetForm):
    def __int__(self, *args, **kwargs):
        super().__init__(self * args, **kwargs)

    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control text-center",
                "type": "email",
                "placeholder": "ایمیل",
                "autofocus": "autofocus",
            }
        ),
    )


class PasswordResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control text-center",
                "placeholder": "رمز عبور جدید",
            }
        )
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control text-center",
                "placeholder": "تکرار رمز عبور جدید",
            }
        )
    )
