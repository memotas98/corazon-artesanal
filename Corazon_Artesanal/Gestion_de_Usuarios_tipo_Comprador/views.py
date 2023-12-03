from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View, generic
from django import forms
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
    return render(request, 'comprador/index.html', {'comprador': comprador})

def LoginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect(f"/comprador/index/{user.pk}")
            else:
                messages.error(request, "Nombre de usuario o contraseña incorrectos.")
    else:
        form = AuthenticationForm()

    return render(request, 'comprador/Inicio_Sesion_Comprador.html', {'form': form})

class RegistroView(generic.CreateView):
    model = Comprador
    template_name = "comprador/registro_Comprador.html"
    form_class = CompradorForm
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data["password"])
        user = form.save()
        return redirect(f"/comprador/index/{user.pk}")

class PerfilComprador(generic.DetailView):
    model = Comprador
    template_name = "comprador/perfil.html"

