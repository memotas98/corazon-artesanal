from django.urls import path
from . import views

app_name = "Gestion_de_Productos"
urlpatterns = [
    path('catalogo/<int:pk>/', views.catalogoView.as_view(), name='catalogo'),
    path('<int:pk>/detalle/<int:id>', views.detalleObra.as_view(), name='detalleObra'),
]