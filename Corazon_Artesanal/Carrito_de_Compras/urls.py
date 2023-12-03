from django.urls import path
from . import views

app_name = "Carrito_de_Compras"
urlpatterns = [
    path('<int:pk>/', views.CarritoView.as_view(), name='verCarrito')
]