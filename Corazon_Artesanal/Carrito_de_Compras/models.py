from django.db import models
from Gestion_de_Usuarios_tipo_Comprador.models import Comprador
from Gestion_de_Inventario.models import Obra

class CarritoCompra(models.Model):
    compradorID = models.ForeignKey(Comprador, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

class DetalleCarrito(models.Model):
    CarritoID = models.ForeignKey(CarritoCompra, on_delete=models.CASCADE)
    obraID = models.ForeignKey(Obra, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
