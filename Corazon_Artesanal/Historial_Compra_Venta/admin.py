from django.contrib import admin
from .models import HistorialCompra, HistorialVenta

# Register your models here.
admin.site.register(HistorialCompra)
admin.site.register(HistorialVenta)