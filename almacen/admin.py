from django.contrib import admin
from .models import(
  CategoriasModel,
  ProductosModel,
  PagosModel,
  BoletasPagoModel,
  ClientesModel,
  DetallesOrdenModel,
  OrdenesModel
)

# Register your models here.

admin.site.register(CategoriasModel)
admin.site.register(ProductosModel)
admin.site.register(PagosModel)
admin.site.register(BoletasPagoModel)
admin.site.register(ClientesModel)
admin.site.register(DetallesOrdenModel)
admin.site.register(OrdenesModel)