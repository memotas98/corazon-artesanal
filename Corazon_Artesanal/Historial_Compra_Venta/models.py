from django.db import models
from Pago_y_Compras.models import Compra

# Create your models here.
class HistorialCompra(models.Model):
    id_Compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    fecha_compra = models.DateTimeField(auto_now_add=True)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    costo_total = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField(max_length=2000)

class HistorialVenta(models.Model):
    id_Compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    fecha_de_venta = models.DateTimeField(auto_now_add=True)
    total_vendido = models.DecimalField(max_digits=10, decimal_places=2)
