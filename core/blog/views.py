# from django.views.generic import ListView, FormView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from . import models
from . import forms
from django.shortcuts import HttpResponse, reverse
from django.urls import reverse


# Create your views here.
class CategoryView(ListView):
    template_name = "blog/categories.html"
    model = models.Category
    paginate_by = 15
    ordering = ["-id"]


class CreateCategoryFormView(CreateView):
    models = models.Category
    form_class = forms.CategoryForm
    template_name = "blog/create_categories.html"
    success_url = "/dashboard/categories/"


def test(request):
    cat = models.Category(title="t1", slug="s1")
    cat.save()
    return HttpResponse("ss")
