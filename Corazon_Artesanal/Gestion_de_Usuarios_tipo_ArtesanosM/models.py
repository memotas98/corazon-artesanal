from django.db import models

# Create your models here.
class InformacionPublica(models.Model):
    nombre = models.CharField(max_length=60)
    telefono = models.CharField(max_length= 10)
    historia = models.TextField(max_length=1000)
    correo_electronico = models.CharField(max_length=50)

class InformacionPrivada(models.Model):
    id_informacion_publica = models.ForeignKey(InformacionPublica)
    fecha_nacimiento = models.DateField()
    contrasena = models.CharField(max_length=8)

