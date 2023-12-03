from django.contrib import admin
from .models import Tarjeta, FormaPago, Compra

# Register your models here.
admin.site.register(Tarjeta)
admin.site.register(FormaPago)
admin.site.register(Compra)