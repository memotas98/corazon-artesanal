from django.db import models
from Gestion_de_Usuarios_tipo_CompradorM.models import Comprador
from Gestion_de_InventarioM.models import Obra 

class Reseña(models.Model):
    id_comprador = models.ForeignKey(Comprador)
    id_obra = models.ForeignKey(Obra)
    descripcion = models.CharField(max_length=300)
    calificacion = models.IntegerField()
    

    