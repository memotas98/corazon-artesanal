from django.shortcuts import render, redirect, get_object_or_404
from django.views import View, generic
from .models import CarritoCompra, DetalleCarrito, Obra

class CarritoView(generic.ListView):
    template_name = "Carrito.html"
    context_object_name = "carrito_list"
    
    def get_queryset(self):
        return CarritoCompra.objects.order_by("fecha_creacion")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['carrito_id'] = self.kwargs.get('pk')
        return context


#def agregar_obra_carrito(request, obra_id):
    #obra = get_object_or_404(Obra, id=obra_id)

    # Obtener o crear el carrito del usuario actual
    #carrito = CarritoCompra.objects.get_or_create(compradorID=request.user.comprador)

    # Agregar la obra al carrito
    #DetalleCarrito.objects.create(CarritoID=carrito, obraID=obra, cantidad=1, subtotal=obra.precio)

    #return redirect('Carrrito.html')


def eliminarCarrito(request, obra_id):
    #obraEliminar = get_object_or_404(Obra, id=obra_id)
    carritoEliminado = CarritoCompra.objects.delete(compradorID=request)
    
