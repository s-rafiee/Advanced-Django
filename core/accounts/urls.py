from django.urls import path, include
from django.contrib.auth.views import LoginView
from .models import models
from . import forms
from . import views

urlpatterns = [
    path('login/', LoginView.as_view(authentication_form=forms.UserLoginForm), name='login'),
    path('dashboard/', views.index , name='dashboard'),
    # path('', include('django.contrib.auth.urls'))
]
