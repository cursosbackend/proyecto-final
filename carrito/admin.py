from django.contrib import admin

from .models import Carrito, CarritoItem


@admin.register(Carrito)
class CarritoAdmin(admin.ModelAdmin):
    list_display = ("id", "usuario", "session_key", "fecha_creacion")


@admin.register(CarritoItem)
class CarritoItemAdmin(admin.ModelAdmin):
    list_display = ("carrito", "producto", "cantidad", "subtotal")
