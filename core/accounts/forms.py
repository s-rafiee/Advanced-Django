from django import forms
from django.contrib.auth.forms import AuthenticationForm


class UserLoginForm(AuthenticationForm):
    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    username = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control text-center', 'type': 'email', 'placeholder': 'ایمیل', 'autofocus': 'autofocus'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control text-center', 'placeholder': 'رمز عبور'}))
