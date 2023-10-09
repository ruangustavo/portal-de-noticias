from blog.models import Postagem
from django.contrib.auth import login, logout
from django.shortcuts import get_object_or_404, redirect, render

from .forms import LoginForm, RegistrationForm
from .models import Autor


def pagina_login(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            return redirect("pagina_inicial")
    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})


def pagina_logout(request):
    logout(request)
    return redirect("pagina_inicial")


def pagina_registrar(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            Autor.objects.create(usuario=usuario)
            login(request, usuario)
            return redirect("pagina_inicial")
    else:
        form = RegistrationForm()
    return render(request, "registrar.html", {"form": form})


def detalhar_autor(request, autor_id):
    autor = get_object_or_404(Autor, id=autor_id)
    postagens = Postagem.objects.filter(autor__id=autor_id)
    context = {"autor": autor, "postagens": postagens}
    return render(request, "detalhar_autor.html", context)
