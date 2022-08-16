from django.shortcuts import HttpResponse
from django.contrib.auth import views as auth_views
from . import forms


class LoginView(auth_views.LoginView):
    form_class = forms.UserLoginForm
    template_name = 'registration/login.html'


class PasswordResetFormView(auth_views.PasswordResetView):
    form_class = forms.PasswordReset
    template_name = 'registration/password_reset_form.html'


class PasswordResetDone(auth_views.PasswordResetDoneView):
    template_name = 'registration/password_reset_done.html'
    form_class = forms.PasswordResetConfirmForm


class PasswordResetConfirmFormView(auth_views.PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'
    form_class = forms.PasswordResetConfirmForm


class PasswordResetComplete(auth_views.PasswordResetCompleteView):
    template_name = 'registration/password_reset_complete.html'


def index(request):
    return HttpResponse(request.user)
