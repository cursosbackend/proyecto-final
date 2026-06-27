from django.urls import path

from . import views

urlpatterns = [
    path("", views.historial_ordenes, name="historial_ordenes"),
    path("confirmar/", views.confirmar_orden, name="confirmar_orden"),
    path("<int:pk>/", views.detalle_orden, name="detalle_orden"),
]
