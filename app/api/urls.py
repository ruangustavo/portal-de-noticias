from django.urls import path

from . import views

urlpatterns = [
    path("temperatura/", views.obter_temperatura, name="receber_temperatura"),
    path("cidade/", views.obter_cidade, name="receber_cidade"),
]
