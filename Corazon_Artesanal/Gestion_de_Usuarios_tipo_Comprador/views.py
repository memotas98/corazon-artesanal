from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View, generic
from django import forms

from Gestion_de_Inventario.models import Obra
from Gestion_de_Usuarios_tipo_Artesanos.models import Artesano
from .models import Comprador
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.forms import AuthenticationForm 

class CompradorForm(forms.ModelForm):
    class Meta:
        model = Comprador
        fields = ['first_name', 'last_name', 'direccion', 'fecha_nacimiento', 'email', 'telefono', 'username', 'password']
        widgets = {'password': forms.PasswordInput}
        
class CompradorLoginForm(forms.ModelForm):
    class Meta:
        model = Comprador
        fields = ['username', 'password']
        widgets = {'password': forms.PasswordInput}

def IndexView(request, pk):
    comprador = get_object_or_404(Comprador, pk=pk)
    obra_list = Obra.objects.order_by("nombre")
    artesano_list = Artesano.objects.order_by("nombre")
    return render(request, 'comprador/index.html', {'comprador': comprador, 'obra_list': obra_list, 'artesano_list': artesano_list})

class PerfilComprador(generic.DetailView):
    model = Comprador
    template_name = "comprador/perfil.html"

def estrategia_registro(request, form_data):
    form = CompradorForm(form_data)
    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data["password"])
        user.save()
        return redirect(f"/comprador/index/{user.pk}")
    return None
 
def estrategia_autenticacion(request):
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(f"/comprador/index/{user.pk}")
    return None

def RegistroView(request):
    if request.method == 'POST':
        result = estrategia_registro(request, request.POST)
        if result:
            return result
    else:
        form = CompradorForm()
    return render(request, 'comprador/registro_Comprador.html', {'form': form})

def LoginView(request):
    if request.method == 'POST':
        result = estrategia_autenticacion(request)
        if result:
            return result
    else:
        form = AuthenticationForm()
    return render(request, 'comprador/Inicio_Sesion_Comprador.html', {'form': form})

class detalleAutor(generic.DetailView):
    model = Artesano
    template_name = "comprador/detalleAutor.html"
    
    def get_object(self, queryset=None):
        return get_object_or_404(Artesano, pk=self.kwargs.get('id'))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comprador_id'] = self.kwargs.get('pk')
        return context
