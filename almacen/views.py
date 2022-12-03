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
  CategoriasModel,
  ProductosModel,
  ClientesModel,
  OrdenesModel,
  DetallesOrdenModel,
  PagosModel,
  BoletasPagoModel,
)

# Create your views here.

class CategoriasView(generics.ListCreateAPIView):
  queryset = CategoriasModel.objects.all()
  serializer_class = CategoriasSerializer

class UpdateCategoriasView(generics.RetrieveUpdateDestroyAPIView):
  queryset = CategoriasModel.objects.all()
  serializer_class = CategoriasSerializer
  http_method_names  = ['get','put','delete']

class ProductosView(generics.ListCreateAPIView):
  queryset = ProductosModel.objects.all()
  serializer_class = ProductosSerializer

class UpdateProductosView(generics.RetrieveUpdateDestroyAPIView):
  queryset = ProductosModel.objects.all()
  serializer_class = ProductosSerializer
  http_method_names  = ['get','put','delete']

class ClientesView(generics.ListCreateAPIView):
  queryset = ClientesModel.objects.all()
  serializer_class = ClientesSerializer

class UpdateClientesView(generics.RetrieveUpdateDestroyAPIView):
  queryset = ClientesModel.objects.all()
  serializer_class = ClientesSerializer
  http_method_names  = ['get','put','delete']

class OrdenesView(generics.ListCreateAPIView):
  queryset = OrdenesModel.objects.all()
  serializer_class = OrdenesSerializer

class UpdateOrdenesView(generics.RetrieveUpdateDestroyAPIView):
  queryset = OrdenesModel.objects.all()
  serializer_class = OrdenesSerializer
  http_method_names  = ['get','put','delete']

class DetallesOrdenView(generics.ListCreateAPIView):
  queryset = DetallesOrdenModel.objects.all()
  serializer_class = DetallesOrdenSerializer

class UpdateDetallesOrdenView(generics.RetrieveUpdateDestroyAPIView):
  queryset = DetallesOrdenModel.objects.all()
  serializer_class = DetallesOrdenSerializer
  http_method_names  = ['get','put','delete']

class PagosView(generics.ListCreateAPIView):
  queryset = PagosModel.objects.all()
  serializer_class = PagosSerializer

class UpdatePagosView(generics.RetrieveUpdateDestroyAPIView):
  queryset = PagosModel.objects.all()
  serializer_class = PagosSerializer
  http_method_names  = ['get','put','delete']

class BoletasPagoView(generics.ListCreateAPIView):
  queryset = BoletasPagoModel.objects.all()
  serializer_class = BoletasPagoSerializer

class UpdateBoletasPagoView(generics.RetrieveUpdateDestroyAPIView):
  queryset = BoletasPagoModel.objects.all()
  serializer_class = BoletasPagoSerializer
  http_method_names  = ['get','put','delete']

# class CategoriasView(generics.ListCreateAPIView):
#   queryset = CategoriasModel.objects.all()
#   serializer_class = CategoriasSerializer

# class UpdateCategoriasView(generics.RetrieveUpdateDestroyAPIView):
#   queryset = CategoriasModel.objects.all()
#   serializer_class = CategoriasSerializer
#   http_method_names  = ['get','put','delete']