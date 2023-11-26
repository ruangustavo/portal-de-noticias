from django.urls import path

from . import views

urlpatterns = [
    path("temperatura/", views.receber_temperatura, name="receber_temperatura"),
]
