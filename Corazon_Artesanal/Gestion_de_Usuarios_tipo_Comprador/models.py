from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Comprador(AbstractUser):
    usuario = models.CharField(max_length=50)
    primernombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=150)
