from django.urls import path, include

urlpatterns = [
    # API URLs
    path("accounts/", include("accounts.api.v1.urls")),
]
