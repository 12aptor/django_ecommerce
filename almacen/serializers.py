from rest_framework import serializers
from .models import (
  CategoriasModel,
  ProductosModel,
  ClientesModel,
  OrdenesModel,
  DetallesOrdenModel,
  PagosModel,
  BoletasPagoModel,
)

class CategoriasSerializer(serializers.ModelSerializer):
  class Meta:
    model = CategoriasModel
    fields = '__all__'

class ProductosSerializer(serializers.ModelSerializer):
  class Meta:
    model = ProductosModel
    fields = '__all__'

class ClientesSerializer(serializers.ModelSerializer):
  class Meta:
    model = ClientesModel
    fields = '__all__'

class OrdenesSerializer(serializers.ModelSerializer):
  class Meta:
    model = OrdenesModel
    fields = '__all__'

class DetallesOrdenSerializer(serializers.ModelSerializer):
  class Meta:
    model = DetallesOrdenModel
    fields = '__all__'

class PagosSerializer(serializers.ModelSerializer):
  class Meta:
    model = PagosModel
    fields = '__all__'

class BoletasPagoSerializer(serializers.ModelSerializer):
  class Meta:
    model = BoletasPagoModel
    fields = '__all__'