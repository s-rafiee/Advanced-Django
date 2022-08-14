from django.shortcuts import HttpResponse
from django.contrib.auth import views as auth_views

from . import forms


class LoginView(auth_views.LoginView):
    form_class = forms.UserLoginForm
    template_name = 'registration/login.html'


def index(request):
    return HttpResponse(request.user)
