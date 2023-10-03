from django.shortcuts import render

from .models import Categoria, Postagem


def pagina_inicial(request):
    categorias = Categoria.objects.all()
    postagens = Postagem.objects.all()
    context = {"categorias": categorias, "postagens": postagens}
    return render(request, "pagina_inicial.html", context)
