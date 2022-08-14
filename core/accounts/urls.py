from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

appname = 'account'
urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('dashboard/logout/', LogoutView.as_view(), name='logout'),


    path('dashboard/', views.index, name='dashboard'),
    # path('', include('django.contrib.auth.urls'))
]
