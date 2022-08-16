from django.shortcuts import render
from django.views.generic import ListView
from . import models


# Create your views here.
class CategoryView(ListView):
    template_name = 'blog/categories.html'
    model = models.Category
