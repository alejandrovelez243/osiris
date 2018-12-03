from django.db import models

# Create your models here.


class Producto(models.Model):
  nombre = models.CharField(max_length=20)
  descripcion = models.TextField(blank=True, null=True)
  activo = models.BooleanField(default=True)
  fecha_ingreso = models.DateTimeField(auto_now_add=True)
  fecha_actualizacion = models.DateTimeField(auto_now=True)

  def __str__(self):
    return str(self.nombre)
