from django.urls import path, include
from django.contrib.auth.views import LogoutView
from . import views

appname = 'accounts'
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('dashboard/logout/', LogoutView.as_view(), name='logout'),

    # Reset Password
    path("password_reset/", views.PasswordResetFormView.as_view(), name="password_reset"),
    path("password_reset/done/", views.PasswordResetDone.as_view(), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", views.PasswordResetConfirmFormView.as_view(), name="password_reset_confirm", ),
    path('password_reset_complete/', views.PasswordResetComplete.as_view(), name='password_reset_complete'),

    # For Dashboard
    path('dashboard/users/', views.UsersViewList.as_view(), name="users"),

    path('dashboard/permissions/', views.PermissionsViewList.as_view(), name="permissions"),
    path('dashboard/groups/', views.GroupsViewList.as_view(), name="groups"),

    # API URLs
    path('api/v1/', include('accounts.api.v1.urls'))
]
