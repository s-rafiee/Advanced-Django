from django.urls import path
from . import views

appname = "blog"
urlpatterns = [
    path("categories/", views.CategoryView.as_view(), name="categories"),
    path(
        "categories/create/",
        views.CreateCategoryFormView.as_view(),
        name="create_categories",
    ),
    path("categories/test/", views.test, name="testcat"),
]
