from django import forms
from . import models


class CategoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
<<<<<<< HEAD
        fields = ["title", "slug", "parent"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control text-center",
                    "placeholder": "عنوان دسته بندی",
                }
            ),
            "slug": forms.TextInput(
                attrs={
                    "class": "form-control text-center",
                    "placeholder": "Slug",
                }
            ),
            "parent": forms.Select(attrs={"class": "form-control"}),
=======
        fields = ['title', 'slug', 'parent']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control text-center', 'placeholder': 'عنوان دسته بندی'}),
            'slug': forms.TextInput(attrs={'class': 'form-control text-center', 'placeholder': 'Slug'}),
            'parent': forms.Select(attrs={'class': 'form-control'}),
>>>>>>> d78be232b16d1b2a980ac2491ed17361dd7eb205
        }

    def clean(self):
        super(CategoryForm, self).clean()
<<<<<<< HEAD
        try:
            self.cleaned_data["parent"] = models.Category.objects.get(
                pk=self.cleaned_data["parent"].id
            )
        except:
            self.cleaned_data["parent"] = None
=======
        print(self.cleaned_data['parent'])
        try:
            self.cleaned_data['parent'] = models.Category.objects.get(pk=self.cleaned_data['parent'].id)
        except:
            self.cleaned_data['parent'] = None
>>>>>>> d78be232b16d1b2a980ac2491ed17361dd7eb205
        return self.cleaned_data
