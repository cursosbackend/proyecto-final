from django.shortcuts import get_object_or_404, render

from .models import Producto


def lista_productos(request):
    productos = Producto.objects.filter(activo=True)
    return render(request, "productos/lista.html", {"productos": productos})


def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk, activo=True)
    return render(request, "productos/detalle.html", {"producto": producto})
