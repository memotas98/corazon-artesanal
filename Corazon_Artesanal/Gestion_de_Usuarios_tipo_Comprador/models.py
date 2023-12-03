from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Comprador(AbstractUser):
    telefono = models.CharField(max_length=10)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    direccion = models.CharField(max_length=150)

