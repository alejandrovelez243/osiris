from django.db import models
from myapps.Inventario.models import Inventario
from myapps.Usuario.models import Usuario
# Create your models here.


class Pedido(models.Model):
  usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
  producto = models.OneToOneField(Inventario, on_delete=models.CASCADE)
  fecha = models.DateField()
  hora = models.TimeField()
  cantidad = models.IntegerField()
  fecha_ingreso = models.DateTimeField(auto_now_add=True)
  fecha_actualizacion = models.DateTimeField(auto_now=True)

  def __str__(self):
    return str(self.usuario)
