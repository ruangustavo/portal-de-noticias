from django.contrib import admin

from .models import Categoria, Postagem


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nome",)


@admin.register(Postagem)
class PostagemAdmin(admin.ModelAdmin):
    list_display = ("titulo", "conteudo", "data_publicacao", "autor")
