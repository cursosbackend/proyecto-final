from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import RegistroForm


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            next_url = request.GET.get("next", "lista_productos")
            return redirect(next_url)
        return render(request, "usuarios/login.html", {"error": "Credenciales inválidas"})
    return render(request, "usuarios/login.html")


def logout_view(request):
    logout(request)
    return redirect("lista_productos")


def registro_view(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("lista_productos")
    else:
        form = RegistroForm()
    return render(request, "usuarios/registro.html", {"form": form})
