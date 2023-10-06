from django.contrib.auth import login
from django.shortcuts import redirect, render

from .forms import LoginForm


def pagina_login(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            login(request, form.get_user())
            return redirect("pagina_inicial")
    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})
