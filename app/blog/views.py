from django.shortcuts import get_object_or_404, render

from .models import Categoria, Postagem

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


def postagens_por_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    postagens = Postagem.objects.filter(categoria=categoria)
    context = {"postagens": postagens, "categoria_atual": categoria}
    return render(request, "postagens_por_categoria.html", context)


def pesquisar_postagens(request):
    termo_pesquisado = request.GET.get("q")
    postagens = (
        Postagem.objects.filter(titulo__icontains=termo_pesquisado)
        if termo_pesquisado
        else Postagem.objects.all()
    )
    context = {"postagens": postagens}
    return render(request, "pesquisar_postagens.html", context)
