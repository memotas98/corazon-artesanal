from django.urls import path
from . import views

urlpatterns = [
    path('loginArtesano/', views.indexView.as_view(template_name='Inicio_Sesion_Artesano.html'), name='loginArtesano'),
    # Agrega otras URL y vistas según sea necesario
]