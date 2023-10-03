from django.shortcuts import render

from .models import Categoria


def pagina_inicial(request):
    categorias = Categoria.objects.all()
    context = {"categorias": categorias}
    return render(request, "pagina_inicial.html", context)
