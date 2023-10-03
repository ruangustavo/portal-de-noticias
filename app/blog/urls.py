from django.urls import path

from . import views

urlpatterns = [
    path("", views.pagina_inicial, name="pagina_inicial"),
    path(
        "postagens/<int:ano>/<int:mes>/",
        views.postagens_por_data,
        name="postagens_por_data",
    ),
]
