from django.urls import path

from . import views

urlpatterns = [
    path("login/", views.pagina_login, name="pagina_login"),
    path("logout/", views.pagina_logout, name="pagina_logout"),
]
