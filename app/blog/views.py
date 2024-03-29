from autor.models import Autor
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CategoriaForm, PostagemForm
from .models import Categoria, Postagem

MAX_POSTAGENS_DESTACADAS = 3
MAX_POSTAGENS_POR_PAGINA = 3


def pagina_inicial(request):
    postagens = Postagem.objects.all()

    paginator = Paginator(postagens, MAX_POSTAGENS_POR_PAGINA)
    pagina = request.GET.get("page")
    postagens_paginadas = paginator.get_page(pagina)

    principal_postagem_destacada = postagens.filter(destaque=True).first()
    postagens_destacadas = postagens.filter(destaque=True)[1:MAX_POSTAGENS_DESTACADAS]

    context = {
        "postagens_paginadas": postagens_paginadas,
        "principal_postagem_destacada": principal_postagem_destacada,
        "postagens_destacadas": postagens_destacadas,
    }
    return render(request, "pagina_inicial.html", context)


def postagens_por_data(request, mes, ano):
    postagens = Postagem.objects.filter(
        data_publicacao__month=mes, data_publicacao__year=ano
    )

    paginator = Paginator(postagens, MAX_POSTAGENS_POR_PAGINA)
    pagina = request.GET.get("page")
    postagens_paginadas = paginator.get_page(pagina)

    context = {"postagens_paginadas": postagens_paginadas}
    return render(request, "postagens_por_data.html", context)


def postagens_por_categoria(request, slug):
    categoria = get_object_or_404(Categoria, slug=slug)
    postagens = Postagem.objects.filter(categoria=categoria)

    paginator = Paginator(postagens, MAX_POSTAGENS_POR_PAGINA)
    pagina = request.GET.get("page")
    postagens_paginadas = paginator.get_page(pagina)

    context = {"postagens_paginadas": postagens_paginadas, "categoria_atual": categoria}
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


def detalhar_postagem(request, slug):
    postagem = get_object_or_404(Postagem, slug=slug)
    context = {"postagem": postagem}
    return render(request, "detalhar_postagem.html", context)


@login_required(login_url="/login/")
def criar_postagem(request):
    if request.method == "POST":
        postagem_form = PostagemForm(request.POST, request.FILES)
        categoria_form = CategoriaForm(request.POST)

        if postagem_form.is_valid() and categoria_form.is_valid():
            postagem = postagem_form.save(commit=False)

            autor = Autor.objects.get(usuario=request.user)
            postagem.autor = autor

            postagem.save()

            categoria_selecionada = categoria_form.cleaned_data.get(
                "categorias_existentes"
            )
            nova_categoria = categoria_form.cleaned_data.get("categoria")

            if categoria_selecionada:
                postagem.categoria.set(categoria_selecionada)

            if nova_categoria:
                categoria = Categoria.objects.create(nome=nova_categoria)
                postagem.categoria.add(categoria)

            return redirect("pagina_inicial")
    else:
        postagem_form = PostagemForm()
        categoria_form = CategoriaForm()

    context = {"postagem_form": postagem_form, "categoria_form": categoria_form}
    return render(request, "criar_ou_editar_postagem.html", context)


@login_required(login_url="/login/")
def editar_postagem(request, slug):
    postagem = get_object_or_404(Postagem, slug=slug)

    if request.method == "POST":
        postagem_form = PostagemForm(request.POST, request.FILES, instance=postagem)
        categoria_form = CategoriaForm(request.POST)

        if postagem_form.is_valid() and categoria_form.is_valid():
            postagem = postagem_form.save(commit=False)

            autor = Autor.objects.get(usuario=request.user)
            postagem.autor = autor

            postagem.save()

            categoria_selecionada = categoria_form.cleaned_data.get(
                "categorias_existentes"
            )
            nova_categoria = categoria_form.cleaned_data.get("categoria")

            if categoria_selecionada:
                postagem.categoria.set(categoria_selecionada)

            if nova_categoria:
                categoria = Categoria.objects.create(nome=nova_categoria)
                postagem.categoria.add(categoria)

            return redirect("pagina_inicial")
    else:
        postagem_form = PostagemForm(instance=postagem)
        categoria_form = CategoriaForm()

    context = {"postagem_form": postagem_form, "categoria_form": categoria_form}
    return render(request, "criar_ou_editar_postagem.html", context)


@login_required(login_url="/login/")
def excluir_postagem(request, slug):
    postagem = get_object_or_404(Postagem, slug=slug)
    postagem.delete()
    return redirect("pagina_inicial")
