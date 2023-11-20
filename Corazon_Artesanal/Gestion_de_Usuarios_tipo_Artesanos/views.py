from django.shortcuts import render, redirect
from django.views import View
from django import forms
from .models import InformacionPublica, InformacionPrivada
from django.contrib.auth import authenticate, login
from django.contrib import messages

class IndexView(View):
    template_name = 'Inicio_Sesion_Artesano.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class LoginForm(forms.ModelForm):
    class Meta:
        model = InformacionPublica, InformacionPrivada
        fields = ['correo_electronico', 'contrasena']
        widgets = {'contrasena': forms.PasswordInput}

class RegisterForm(forms.ModelForm):
    class Meta:
        model = InformacionPublica, InformacionPrivada
        fields = ['nombre', 'telefono', 'historia', 'fecha_nacimiento', 'correo_electronico', 'contrasena']
        widgets = {'contrasena': forms.PasswordInput}

class LoginView(View):
    template_name = 'Inicio_Sesion_Artesano.html'

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            correo_electronico = form.cleaned_data['correo_electronico']
            contrasena = form.cleaned_data['contrasena']

            user = authenticate(request, correo_electronico=correo_electronico, contrasena=contrasena)

            if user is not None:
                login(request, user)
                messages.success(request, 'Se ha Iniciado sesión')
                return redirect('index.html') 
            else:
                messages.error(request, 'Inicio de sesión fallido. Por favor, verifica que este correcta la información.')
        return render(request, self.template_name, {'form': form})

class RegisterView(View):
    template_name = 'registro_Artesano.html'

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Inicio_Sesion_Artesano.html')  
        else:
            return render(request, self.template_name, {'form': form})
