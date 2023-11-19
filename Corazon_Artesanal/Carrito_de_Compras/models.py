from django.db import models
from Gestion_de_Usuarios_tipo_CompradorM.models import Comprador
from Gestion_de_InventarioM.models import Obra

class CarritoCompra(models.Model):
    compradorID = models.ForeignKey(Comprador)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

class DetalleCarrito(models.Model):
    CarritoID = models.ForeignKey(CarritoCompra)
    obraID = models.ForeignKey(Obra)
    cantidad = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
