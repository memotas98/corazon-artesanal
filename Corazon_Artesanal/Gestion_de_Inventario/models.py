from django.db import models
from Gestion_de_Usuarios_tipo_Artesanos.models import InformacionPublica

class Obra(models.Model):
    id_artesano = models.ForeignKey(InformacionPublica, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=7, decimal_places=2)
    descripcion = models.CharField(max_length=300)
    proceso_creativo = models.CharField(max_length=50)
