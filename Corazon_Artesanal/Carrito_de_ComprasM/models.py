from django.db import models

class Obra(models.Model):
    id_obra = models.IntegerField(unique=True)
    id_artesano = models.IntegerField(unique=True)
    nombre = models.CharField(max_length="50")
    precio_decimal = models.DecimalField(max_digits="7", decimal_places="2")
    descripcion = models.CharField(max_length="300")
    proceso_creatio = models.CharField(max_length="50")
    
    
    def __str__(self):
        return self.nombre
