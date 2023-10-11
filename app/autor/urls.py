from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.pagina_login, name="pagina_login"),
    path("logout/", views.pagina_logout, name="pagina_logout"),
    path("registrar/", views.pagina_registrar, name="pagina_registrar"),
    path("autor/<int:autor_id>", views.detalhar_autor, name="detalhar_autor"),
    path("atualizar-perfil/", views.atualizar_perfil, name="atualizar_perfil"),
]
