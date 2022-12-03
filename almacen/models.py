from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class CategoriasModel(models.Model):
  id = models.AutoField(primary_key=True)
  nombre = models.CharField(max_length=45)
  descripcion = models.CharField(max_length=100)
  estado = models.BooleanField(default=True)

  class Meta:
    db_table = "categorias"

class ProductosModel(models.Model):
  id = models.AutoField(primary_key=True)
  nombre = models.CharField(max_length=45)
  marca = models.CharField(max_length=45)
  talla = models.CharField(max_length=45)
  codigo = models.CharField(max_length=45)
  imagen = models.TextField()
  precio = models.FloatField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now_add=True)
  estado = models.BooleanField(default=True)
  categoria_id = models.ForeignKey(
    CategoriasModel,
    on_delete=models.CASCADE
  )

  class Meta:
    db_table = "productos"

class ClientesModel(models.Model):
  id = models.AutoField(primary_key=True)
  nombre = models.CharField(max_length=45)
  apellido = models.CharField(max_length=45)
  correo = models.CharField(max_length=100)
  dni = models.IntegerField()
  estado = models.BooleanField(default=True)

  class Meta:
    db_table = "clientes"


class OrdenesModel(models.Model):
  id = models.AutoField(primary_key=True)
  observacion = models.CharField(max_length=100)
  estado = models.BooleanField(default=True)
  cliente_id = models.ForeignKey(
    ClientesModel,
    on_delete=models.CASCADE
  )
  usuario_id = models.ForeignKey(
    User,
    on_delete=models.CASCADE
  )

  class Meta:
    db_table = "ordenes"

class DetallesOrdenModel(models.Model):
  id = models.AutoField(primary_key=True)
  cantidad = models.IntegerField()
  orden_id = models.ForeignKey(
    OrdenesModel,
    on_delete=models.CASCADE
  )
  producto_id = models.ForeignKey(
    ProductosModel,
    on_delete=models.CASCADE
  )

  class Meta:
    db_table = "ordenes_detalle"

class PagosModel(models.Model):
  id = models.AutoField(primary_key=True)
  monto = models.FloatField()
  estado = models.BooleanField(default=True)
  orden_id = models.ForeignKey(
    OrdenesModel,
    on_delete=models.CASCADE
  )

  class Meta:
    db_table = "pagos"

class BoletasPago(models.Model):
  id = models.AutoField(primary_key=True)
  codigo = models.CharField(max_length=45)
  total = models.FloatField()
  estado = models.BooleanField(default=True)
  pago_id = models.ForeignKey(
    PagosModel,
    on_delete=models.CASCADE
  )

  class Meta:
    db_table = "botelas_pago"

