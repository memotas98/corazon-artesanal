from django.db import models

class Obra(models.Model):
    id_obra = models.AutoField(primary_key=True)
    id_artesano = models.ForeignKey(InformacionPrivada)
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=7, decimal_places=2)
    descripcion = models.CharField(max_length=300)
    proceso_creativo = models.CharField(max_length=50)
