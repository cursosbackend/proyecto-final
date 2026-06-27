from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from productos.models import Producto

from .models import Carrito, CarritoItem


def get_or_create_carrito(request):
    if request.user.is_authenticated:
        carrito, _ = Carrito.objects.get_or_create(usuario=request.user)
    else:
        session_key = request.session.session_key
        if not session_key:
            request.session.save()
            session_key = request.session.session_key
        carrito, _ = Carrito.objects.get_or_create(session_key=session_key)
    return carrito


def ver_carrito(request):
    carrito = get_or_create_carrito(request)
    items = carrito.items.select_related("producto").all()
    total = sum(item.subtotal() for item in items)
    return render(request, "carrito/ver.html", {"carrito": carrito, "items": items, "total": total})


@login_required
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id, activo=True)
    carrito = get_or_create_carrito(request)
    item, created = CarritoItem.objects.get_or_create(carrito=carrito, producto=producto)
    if not created:
        if item.cantidad < producto.stock:
            item.cantidad += 1
            item.save()
    return redirect("ver_carrito")


@login_required
def quitar_del_carrito(request, item_id):
    item = get_object_or_404(CarritoItem, pk=item_id, carrito__usuario=request.user)
    item.delete()
    return redirect("ver_carrito")


@login_required
def actualizar_cantidad(request, item_id):
    item = get_object_or_404(CarritoItem, pk=item_id, carrito__usuario=request.user)
    if request.method == "POST":
        cantidad = int(request.POST.get("cantidad", 1))
        if cantidad > 0 and cantidad <= item.producto.stock:
            item.cantidad = cantidad
            item.save()
        elif cantidad == 0:
            item.delete()
    return redirect("ver_carrito")
