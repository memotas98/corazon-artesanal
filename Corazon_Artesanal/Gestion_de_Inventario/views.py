from django.shortcuts import render, redirect, get_object_or_404
from .models import Obra
from Gestion_de_Usuarios_tipo_Artesanos.models import Artesano
from django import forms


# Create your views here.
class ObraForm(forms.ModelForm):
    class Meta:
        model = Obra
        fields = ['nombre', 'precio', 'descripcion', 'proceso_creativo', 'cantidadExistente']
        widgets = {
            'nombre': forms.TextInput(attrs={'required': False}),
            'precio': forms.TextInput(attrs={'required': False}),
            'descripcion': forms.TextInput(attrs={'required': False}),
            'proceso_creativo': forms.TextInput(attrs={'required': False}),
            'cantidadExistente': forms.TextInput(attrs={'required': False})
        }

def indexObraView(request, pk):
    form = ObraForm(request.POST)
    artesano = get_object_or_404(Artesano, pk=pk)
    return render(request, 'inventario/creacionObra.html', {'form': form, 'artesano': artesano})

def crearObra(request, pk):
    artesano = get_object_or_404(Artesano, pk=pk)
    
    if request.method == 'POST':
        form = ObraForm(request.POST)
        if form.is_valid():
            nueva_obra = form.save(commit=False)
            nueva_obra.id_artesano = artesano  # Asumiendo que tu modelo Obra tiene 'artesano' como ForeignKey
            nueva_obra.save()
    # if request.method == 'POST':
    #     form = ObraForm(request.POST)
        
    #     if form.is_valid():
    #         nombre = form.cleaned_data['nombre']
    #         precio = form.cleaned_data['precio']
    #         descripcion = form.cleaned_data['descripcion']
    #         proceso_creativo = form.cleaned_data['proceso_creativo']
    #         cantidadExistente = form.cleaned_data['cantidadExistente']
    #         id_artesano = pk
            
    #         nueva_obra = form.save(commit=False)
    #         nueva_obra.id_artesano = id_artesano
    #         nueva_obra.save()
            return redirect(f"/artesano/index/{pk}")
    else:
        form = ObraForm()

    return render(request, 'inventario/creacionObra.html', {'form': form})