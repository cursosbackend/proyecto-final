from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .models import Orden


@login_required
def confirmar_orden(request):
    from carrito.models import Carrito
    from carrito.views import get_or_create_carrito

    carrito = get_or_create_carrito(request)
    items = carrito.items.select_related("producto").all()

    if not items:
        return redirect("ver_carrito")

    orden = Orden.objects.create(usuario=request.user)
    total = 0
    for item in items:
        orden.items.create(
            producto=item.producto,
            cantidad=item.cantidad,
            precio_unitario=item.producto.precio,
        )
        producto = item.producto
        producto.stock -= item.cantidad
        producto.save()
        total += item.subtotal()

    orden.total = total
    orden.save()
    carrito.items.all().delete()

    return redirect("detalle_orden", pk=orden.pk)


@login_required
def historial_ordenes(request):
    ordenes = Orden.objects.filter(usuario=request.user).prefetch_related("items").all()
    return render(request, "pedidos/historial.html", {"ordenes": ordenes})


@login_required
def detalle_orden(request, pk):
    orden = get_object_or_404(Orden, pk=pk, usuario=request.user)
    return render(request, "pedidos/detalle.html", {"orden": orden})
