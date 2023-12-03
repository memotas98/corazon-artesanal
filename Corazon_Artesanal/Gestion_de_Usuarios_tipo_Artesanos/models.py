from django.db import models

# Create your models here.
class Artesano(models.Model):
    fecha_nacimiento = models.DateField()
    contraseña = models.CharField(max_length=8)
    nombre = models.CharField(max_length=60)
    telefono = models.CharField(max_length= 10)
    historia = models.TextField(max_length=1000)
    correo_electronico = models.CharField(max_length=50)

