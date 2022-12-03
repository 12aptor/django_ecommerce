from .views import (
  CategoriasView, UpdateCategoriasView,
  ProductosView, UpdateProductosView,
  ClientesView, UpdateClientesView,
  OrdenesView, UpdateOrdenesView,
  DetallesOrdenView, UpdateDetallesOrdenView,
  PagosView, UpdatePagosView,
  BoletasPagoView, UpdateBoletasPagoView,
)
from django.urls import path


urlpatterns = [
  path('categorias', CategoriasView.as_view()),
  path('categorias/<pk>', UpdateCategoriasView.as_view()),
  path('productos', ProductosView.as_view()),
  path('productos/<pk>', UpdateProductosView.as_view()),
  path('clientes', ClientesView.as_view()),
  path('clientes/<pk>', UpdateClientesView.as_view()),
  path('ordenes', OrdenesView.as_view()),
  path('ordenes/<pk>', UpdateOrdenesView.as_view()),
  path('detalles_orden', DetallesOrdenView.as_view()),
  path('detalles_orden/<pk>', UpdateDetallesOrdenView.as_view()),
  path('pagos', PagosView.as_view()),
  path('pagos/<pk>', UpdatePagosView.as_view()),
  path('boletas_pago', BoletasPagoView.as_view()),
  path('boletas_pago/<pk>', UpdateBoletasPagoView.as_view()),
]