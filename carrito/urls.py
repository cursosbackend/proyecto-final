from django.urls import path

from . import views

urlpatterns = [
    path("", views.ver_carrito, name="ver_carrito"),
    path("agregar/<int:producto_id>/", views.agregar_al_carrito, name="agregar_al_carrito"),
    path("quitar/<int:item_id>/", views.quitar_del_carrito, name="quitar_del_carrito"),
    path("actualizar/<int:item_id>/", views.actualizar_cantidad, name="actualizar_cantidad"),
]
