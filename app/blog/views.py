from django.shortcuts import render

from .models import Categoria, Postagem

MAX_PAGINAS_DESTACADAS = 2


def pagina_inicial(request):
    categorias = Categoria.objects.all()
    postagens = Postagem.objects.all()
    postagens_destacadas_recente = postagens.filter(destaque=True)[
        :MAX_PAGINAS_DESTACADAS
    ]

    context = {
        "categorias": categorias,
        "postagens": postagens,
        "postagens_destacadas": postagens_destacadas_recente,
    }
    return render(request, "pagina_inicial.html", context)
