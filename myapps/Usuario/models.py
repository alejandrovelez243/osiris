from django.db import models
from django.contrib.auth.models import User
from myapps.Empresa.models import Empresa

# Create your models here.


def get_first_name(self):
    return self.first_name + " " + self.last_name


User.add_to_class("__str__", get_first_name)

class Usuario(models.Model):
  usuario = models.OneToOneField(User, on_delete=models.CASCADE)
  empresa = models.OneToOneField(
      Empresa, on_delete=models.CASCADE)
  documento = models.CharField(max_length=15)
  telefono = models.CharField(max_length=15)
  direccion = models.CharField(max_length=20)
  fecha_ingreso = models.DateTimeField(auto_now_add=True)
  fecha_actualizacion = models.DateTimeField(auto_now=True)

  def __str__(self):
    return str(self.usuario)
