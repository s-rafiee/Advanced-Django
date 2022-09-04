from django.urls import path
from . import views

appname = "blog"
urlpatterns = [
<<<<<<< HEAD
    path("categories/", views.CategoryView.as_view(), name="categories"),
    path(
        "categories/create/",
        views.CreateCategoryFormView.as_view(),
        name="create_categories",
    ),
    path("categories/test/", views.test, name="testcat"),
=======
    path('categories/', views.CategoryView.as_view(), name='categories'),
    path('categories/create/', views.CreateCategoryFormView.as_view(), name='create_categories'),
    path('categories/test/', views.test, name='testcat'),
>>>>>>> d78be232b16d1b2a980ac2491ed17361dd7eb205
]
