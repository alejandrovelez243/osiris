from django.db import models
from myapps.Productos.models import Producto
from myapps.Empresa.models import Empresa
# Create your models here.


class Inventario(models.Model):
  producto = models.OneToOneField(
      Producto, on_delete=models.CASCADE)
  empresa = models.OneToOneField(
      Empresa, on_delete=models.CASCADE)
  valor_compra = models.IntegerField()
  valor_venta = models.IntegerField()
  ganancia = models.FloatField()
  cantidad = models.IntegerField()
  activo = models.BooleanField(default=True)
  fecha_ingreso = models.DateTimeField(auto_now_add=True)
  fecha_actualizacion = models.DateTimeField(auto_now=True)

  def __str__(self):
    return str(self.producto)
