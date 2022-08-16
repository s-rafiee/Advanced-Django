from django.urls import path
from . import views

appname = 'blog'
urlpatterns = [
    path('categories/', views.CategoryView.as_view(), name='categories'),
]
