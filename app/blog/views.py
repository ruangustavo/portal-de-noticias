from django.shortcuts import render

from .models import Postagem

MAX_POSTAGENS_DESTACADAS = 3


def pagina_inicial(request):
    postagens = Postagem.objects.all()
    principal_postagem_destacada = postagens.filter(destaque=True).first()
    postagens_destacadas = postagens.filter(destaque=True)[1:MAX_POSTAGENS_DESTACADAS]

    context = {
        "postagens": postagens,
        "principal_postagem_destacada": principal_postagem_destacada,
        "postagens_destacadas": postagens_destacadas,
    }
    return render(request, "pagina_inicial.html", context)


def postagens_por_data(request, mes, ano):
    postagens = Postagem.objects.filter(
        data_publicacao__month=mes, data_publicacao__year=ano
    )
    context = {"postagens": postagens}
    return render(request, "postagens_por_data.html", context)
