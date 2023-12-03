from django.shortcuts import render, redirect, get_object_or_404
from django.views import View, generic
from django import forms
from .models import Artesano
from django.contrib.auth import authenticate, login
from django.contrib import messages

class ArtesanoForm(forms.ModelForm):
    class Meta:
        model = Artesano
        fields = ['nombre', 'telefono', 'historia', 'fecha_nacimiento', 'correo_electronico', 'contraseña']
        widgets = {'contraseña': forms.PasswordInput}
        
class ArtesanoLoginForm(forms.ModelForm):
    class Meta:
        model = Artesano
        fields = ['correo_electronico', 'contraseña']
        widgets = {'contraseña': forms.PasswordInput}

def IndexView(request, pk):
    artesano = get_object_or_404(Artesano, pk=pk)
    return render(request, 'artesano/index.html', {'artesano': artesano})

def LoginView(request):
    if request.method == 'POST':
        form = ArtesanoLoginForm(request.POST)
        
        if form.is_valid():
            correo_electronico = form.cleaned_data['correo_electronico']
            contrasena = form.cleaned_data['contraseña']

            autenticacion = Artesano.objects.filter(correo_electronico=correo_electronico, contraseña=contrasena)

            if autenticacion.exists():
                artesano = autenticacion.first()
                return redirect(f"/artesano/index/{artesano.pk}")
    else:
        form = ArtesanoLoginForm()

    return render(request, 'artesano/Inicio_Sesion_Artesano.html', {'form': form})

class RegistroView(generic.CreateView):
    model = Artesano
    template_name = "artesano/registro_Artesano.html"
    fields = ['nombre', 'telefono', 'historia', 'fecha_nacimiento', 'correo_electronico', 'contraseña']
    
    def form_valid(self, form):
        nuevo_artesano = form.save()
        return redirect(f"/artesano/index/{nuevo_artesano.pk}")

class PerfilArtesano(generic.DetailView):
    model = Artesano
    template_name = "artesano/perfil.html"
