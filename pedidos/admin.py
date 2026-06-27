from django.contrib import admin

from .models import Orden, OrdenItem


class OrdenItemInline(admin.TabularInline):
    model = OrdenItem
    readonly_fields = ("producto", "cantidad", "precio_unitario", "subtotal")
    can_delete = False


@admin.register(Orden)
class OrdenAdmin(admin.ModelAdmin):
    list_display = ("id", "usuario", "fecha", "total", "estado")
    list_filter = ("estado", "fecha")
    inlines = [OrdenItemInline]


@admin.register(OrdenItem)
class OrdenItemAdmin(admin.ModelAdmin):
    list_display = ("orden", "producto", "cantidad", "precio_unitario", "subtotal")
