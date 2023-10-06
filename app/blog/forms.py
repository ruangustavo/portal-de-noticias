from ckeditor.widgets import CKEditorWidget
from django import forms

from .models import Categoria, Postagem


class PostagemForm(forms.ModelForm):
    class Meta:
        model = Postagem
        fields = ("titulo", "conteudo", "destaque", "imagem")
        widgets = {
            "titulo": forms.TextInput(attrs={"class": "form-control"}),
            "conteudo": forms.CharField(widget=CKEditorWidget()),
            "destaque": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "imagem": forms.FileInput(attrs={"class": "form-control"}),
        }


class CategoriaForm(forms.Form):
    categoria = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    categorias_existentes = forms.ChoiceField(
        choices=[
            (categoria.id, categoria.nome) for categoria in Categoria.objects.all()
        ],
        widget=forms.Select(attrs={"class": "form-control"}),
        required=False,
    )
