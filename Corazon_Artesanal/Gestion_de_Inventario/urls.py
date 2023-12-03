from django.urls import path
from . import views

app_name = "Gestion_de_Inventario"
urlpatterns = [
    path('<int:pk>/', views.indexObraView, name='indexObra'),
    path('agregar/<int:pk>/', views.crearObra, name='agregarObra')
]