from django.db import models
from Gestion_de_Usuarios_tipo_CompradorM.models import Comprador
from Carrito_de_Compras.models import CarritoCompra

# Create your models here.
class FormaPago(models.Model):
    tipo_pago = models.CharField(max_length=80)

class Targeta(models.Model):
    idFormaPago = models.ForeignKey(FormaPago)
    numeroTargeta = models.IntegerField(max_length=16)
    codigoSeguridad = models.CharField(max_length=3)
    fechaExpiracion = models.DateField()
    nombreTitular = models.CharField(max_length=100)
    bancoAdquiriente = models.CharField(max_length=50)

class Compra(models.Model):
    idComprador = models.ForeignKey(Comprador)
    idCarritoCompras = models.ForeignKey(CarritoCompra)
    formaPagoId = models.ForeignKey(FormaPago)
    fechaCompra = models.DateField()
    montoTotal = models.FloatField()
    direccionEnvio = models.CharField(max_length=100)
    numeroSeguimiento = models.CharField(max_length=10)
    observaciones = models.TextField(max_length=100)