from django.shortcuts import render

from .models import Categoria, Postagem

MAX_PAGINAS_DESTACADAS = 2
MAX_PAGINAS_RECENTES = 5


def pagina_inicial(request):
    categorias = Categoria.objects.all()
    postagens = Postagem.objects.all()
    postagens_destacadas = postagens.filter(destaque=True)[:MAX_PAGINAS_DESTACADAS]
    postagens_recentes = postagens.order_by("-data_publicacao")[:MAX_PAGINAS_RECENTES]

    context = {
        "categorias": categorias,
        "postagens": postagens,
        "postagens_destacadas": postagens_destacadas,
        "postagens_recentes": postagens_recentes,
    }
    return render(request, "pagina_inicial.html", context)
