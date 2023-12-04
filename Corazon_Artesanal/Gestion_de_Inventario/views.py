from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Obra
from Gestion_de_Usuarios_tipo_Artesanos.models import Artesano
from django import forms
from django.views import generic
from django.urls import reverse, reverse_lazy


# Create your views here.
class ObraForm(forms.ModelForm):
    class Meta:
        model = Obra
        fields = ['nombre', 'precio', 'descripcion', 'proceso_creativo', 'cantidadExistente']

def indexObraView(request, pk):
    form = ObraForm(request.POST)
    artesano = get_object_or_404(Artesano, pk=pk)
    return render(request, 'inventario/creacionObra.html', {'form': form, 'artesano': artesano})

def crearObra(request, pk):
    artesano = get_object_or_404(Artesano, pk=pk)
    
    if request.method == 'POST':
        form = ObraForm(request.POST)
        
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            precio = form.cleaned_data['precio']
            descripcion = form.cleaned_data['descripcion']
            proceso_creativo = form.cleaned_data['proceso_creativo']
            cantidadExistente = form.cleaned_data['cantidadExistente']
            id_artesano = artesano
            
            nueva_obra = Obra(id_artesano=id_artesano, nombre=nombre, precio=precio, descripcion=descripcion, proceso_creativo=proceso_creativo, cantidadExistente=cantidadExistente)
            nueva_obra.save()
            return redirect(f"/obra/inventario/{pk}")
    else:
        form = ObraForm()

    return render(request, 'inventario/creacionObra.html', {'form': form})

class inventarioView(generic.ListView):
    template_name = "inventario/inventario.html"
    context_object_name = "obra_list"
    
    def get_queryset(self):
        return Obra.objects.order_by("nombre")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['artesano_id'] = self.kwargs.get('pk')
        return context
    
class detalleObra(generic.DetailView):
    model = Obra
    template_name = "inventario/detalleObra.html"
    
    def get_object(self, queryset=None):
        return get_object_or_404(Obra, pk=self.kwargs.get('id'))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['artesano_id'] = self.kwargs.get('pk')
        return context
    
class actualizarObra(generic.UpdateView):
    model = Obra
    fields = ['nombre', 'precio', 'descripcion', 'proceso_creativo', 'cantidadExistente']
    template_name = "inventario/editarObra.html"
    
    def get_object(self, queryset=None):
        return get_object_or_404(Obra, pk=self.kwargs.get('id'))
    
    def obtenerArtesano(self):
        artesano = get_object_or_404(Artesano, pk=self.kwargs.get('pk'))
        return artesano
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['artesano_id'] = self.kwargs.get('pk')
        return context
    
    def form_valid(self, form):
        form.save()
        artesano = self.obtenerArtesano()
        return redirect(reverse('Gestion_de_Inventario:inventario', kwargs={'pk': artesano.pk}))
    
class borrarObra(generic.DeleteView):
    model = Obra
    
    def get_success_url(self):
        artesano = self.obtenerArtesano()
        return reverse_lazy("Gestion_de_Inventario:inventario", kwargs={'pk': artesano.pk})
    
    def obtenerArtesano(self):
        artesano = get_object_or_404(Artesano, pk=self.kwargs.get('pk'))
        return artesano
    
    def get_object(self, queryset=None):
        return get_object_or_404(Obra, pk=self.kwargs.get('id'))
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())
    