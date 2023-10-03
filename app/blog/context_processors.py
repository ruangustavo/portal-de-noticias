from .models import Categoria, Postagem

MAX_POSTAGENS_RECENTES = 5


def postagem_context(request):
    postagens = Postagem.objects.all()
    categorias = Categoria.objects.all()
    data_postagens_recentes = postagens.dates("data_publicacao", "month", order="DESC")
    postagens_recentes = postagens.order_by("-data_publicacao")[:MAX_POSTAGENS_RECENTES]

    context = {
        "categorias": categorias,
        "postagens_recentes": postagens_recentes,
        "data_postagens_recentes": data_postagens_recentes,
    }
    return context
