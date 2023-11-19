from django.db import models
from Gestion_de_Usuarios_tipo_Comprador.models import Comprador
from Gestion_de_Inventario.models import Obra 

class Reseña(models.Model):
    id_comprador = models.ForeignKey(Comprador, on_delete=models.CASCADE)
    id_obra = models.ForeignKey(Obra, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=300)
    calificacion = models.IntegerField()
    

    