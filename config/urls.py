from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("productos/", include("productos.urls")),
    path("cuentas/", include("usuarios.urls")),
    path("carrito/", include("carrito.urls")),
    path("pedidos/", include("pedidos.urls")),
    path("", RedirectView.as_view(pattern_name="lista_productos", permanent=False)),
]
