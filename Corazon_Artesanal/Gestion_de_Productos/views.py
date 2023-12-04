from django import forms
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import generic
from Gestion_de_Usuarios_tipo_Comprador.models import Comprador
from .models import Obra, Reseña

# Create your views here.
class catalogoView(generic.ListView):
    template_name = "productos/catalogo.html"
    context_object_name = "obra_list"
    
    def get_queryset(self):
        return Obra.objects.order_by("nombre")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['comprador_id'] = self.kwargs.get('pk')
        return context
    
class ReseñaForm(forms.ModelForm):
    class Meta:
        model = Reseña
        fields = ['descripcion', 'calificacion']
    
class DetalleObraYReseñas(generic.DetailView, generic.edit.FormMixin):
    model = Obra
    template_name = "productos/detalleObra.html"
    form_class = ReseñaForm
    context_object_name = "obra"
    
    def get_object(self, queryset=None):
        return get_object_or_404(Obra, pk=self.kwargs.get('id'))

    def get_success_url(self):
        return reverse_lazy('Gestion_de_Productos:detalleObra', kwargs={'pk': self.kwargs['pk'], 'id': self.kwargs['id']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        context['reseña_list'] = Reseña.objects.filter(id_obra=self.object).order_by("-calificacion")
        context['comprador_id'] = self.kwargs.get('pk')
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        comprador = get_object_or_404(Comprador, pk=self.kwargs['pk'])
        form.instance.id_comprador = comprador
        form.instance.id_obra = self.object
        form.save()
        return super().form_valid(form)