from django.db import models

# Create your models here.

class Empresa(models.Model):
  nombre = models.CharField(max_length=30)
  nit = models.CharField(max_length=15)
  telefono = models.CharField(max_length=15)
  direccion = models.CharField(max_length=20)
  activo = models.BooleanField(default=True)
  fecha_ingreso = models.DateTimeField(auto_now_add=True)
  fecha_actualizacion = models.DateTimeField(auto_now=True)

  def __str__(self):
    return str(self.nombre)
