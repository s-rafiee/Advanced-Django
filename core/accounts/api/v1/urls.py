from django.urls import path
from . import views

# from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path('accounts/register/', views.RegistrationAPIView.as_view(), name='api_registration'),
    path('accounts/login/', views.LoginTokenView.as_view(), name='api_token_login'),  # Login with token
    path('accounts/logout/', views.LogoutTokenView.as_view(), name='api_token_logout'),  # Login with token
]
