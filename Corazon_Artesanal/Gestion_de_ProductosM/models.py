from django.db import models

class Reseña(models.Model):
    id_Reseña = models.AutoField(primary_key=True)
    id_comprador = models.ForeignKey(Comprador)
    id_obra = models.ForeignKey(Obra)
    descripcion = models.CharField(max_length=300)
    

    