from django.shortcuts import get_object_or_404, render
from django.views import generic
from .models import Obra

# Create your views here.
class catalogoView(generic.ListView):
    template_name = "productos/catalogo.html"
    context_object_name = "obra_list"
    
    def get_queryset(self):
        return Obra.objects.order_by("-nombre")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['comprador_id'] = self.kwargs.get('pk')
        return context
    
class detalleObra(generic.DetailView):
    model = Obra
    template_name = "productos/detalleObra.html"
    
    def get_object(self, queryset=None):
        return get_object_or_404(Obra, pk=self.kwargs.get('id'))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comprador_id'] = self.kwargs.get('pk')
        return context