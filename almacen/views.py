from rest_framework import generics
from .serializers import (
  CategoriasSerializer,
  ProductosSerializer,
  ClientesSerializer,
  OrdenesSerializer,
  DetallesOrdenSerializer,
  PagosSerializer,
  BoletasPagoSerializer
)

from .models import (
  CategoriasModel
)

# Create your views here.

class CategoriasView(generics.ListCreateAPIView):
  queryset = CategoriasModel.objects.all()
  serializer_class = CategoriasSerializer