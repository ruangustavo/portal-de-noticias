from django.urls import path

from . import views

urlpatterns = [
    path("", views.pagina_inicial, name="pagina_inicial"),
    path(
        "postagens/criar/",
        views.criar_postagem,
        name="criar_ou_editar_postagem.html",
    ),
    path(
        "postagens/<slug:slug>/",
        views.detalhar_postagem,
        name="detalhar_postagem",
    ),
    path(
        "postagens/<int:ano>/<int:mes>/",
        views.postagens_por_data,
        name="postagens_por_data",
    ),
    path(
        "categorias/<slug:slug>/",
        views.postagens_por_categoria,
        name="postagens_por_categoria",
    ),
    path("pesquisar/", views.pesquisar_postagens, name="pesquisar_postagens"),
    path(
        "postagens/<slug:slug>/editar/",
        views.editar_postagem,
        name="editar_postagem",
    ),
    path(
        "postagens/<slug:slug>/excluir/",
        views.excluir_postagem,
        name="excluir_postagem",
    ),
]
