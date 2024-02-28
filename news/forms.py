from django import forms
from news.models import Category, News


class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        labels = {"name": "Nome"}


class CreateNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = [
            "title",
            "content",
            "author",
            "created_at",
            "image",
            "categories",
        ]
        labels = {
            "title": "Título",
            "content": "Conteúdo",
            "author": "Autoria",
            "created_at": "Criado em",
            "image": "URL da Imagem",
        }
        widgets = {
            "author": forms.Select,
            "categories": forms.CheckboxSelectMultiple,
            "created_at": forms.DateInput(attrs={"type": "date"}),
        }
