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
<<<<<<< HEAD
    ordering = ["-id"]
=======
    ordering = ['-id']
>>>>>>> d78be232b16d1b2a980ac2491ed17361dd7eb205


class CreateCategoryFormView(CreateView):
    models = models.Category
    form_class = forms.CategoryForm
<<<<<<< HEAD
    template_name = "blog/create_categories.html"
    success_url = "/dashboard/categories/"


def test(request):
    cat = models.Category(title="t1", slug="s1")
    cat.save()
    return HttpResponse("ss")
=======
    template_name = 'blog/create_categories.html'
    success_url = '/dashboard/categories/'


def test(request):
    cat = models.Category(title='t1', slug='s1')
    cat.save()
    return HttpResponse('ss')
>>>>>>> d78be232b16d1b2a980ac2491ed17361dd7eb205
