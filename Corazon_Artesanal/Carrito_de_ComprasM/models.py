from django.db import models
from Gestion_de_Usuarios_tipo_CompradorM.models import Comprador

class CarritoCompra(models.Model):
    CarritoID = models.AutoField(primary_key=True)
    comprador = models.ForeignKey(Comprador)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

class DetalleCarrito(models.Model):
    DetalleCarritoID = models.AutoField(primary_key=True)
    CarritoID = models.ForeignKey(CarritoCompra)
    obra = models.ForeignKey(Obra)
    cantidad = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    
