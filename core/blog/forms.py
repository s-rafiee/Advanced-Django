from django import forms
from . import models


class CategoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = ['title', 'slug', 'parent']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control text-center', 'placeholder': 'عنوان دسته بندی'}),
            'slug': forms.TextInput(attrs={'class': 'form-control text-center', 'placeholder': 'Slug'}),
            'parent': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean(self):
        super(CategoryForm, self).clean()
        print(self.cleaned_data['parent'])
        try:
            self.cleaned_data['parent'] = models.Category.objects.get(pk=self.cleaned_data['parent'].id)
        except:
            self.cleaned_data['parent'] = None
        return self.cleaned_data
