from django.urls import path
from . import views

app_name = "Gestion_de_Inventario"
urlpatterns = [
    path('<int:pk>/', views.indexObraView, name='indexObra'),
    path('agregar/<int:pk>/', views.crearObra, name='agregarObra'),
    path('inventario/<int:pk>/', views.inventarioView.as_view(), name='inventario'),
    path("<int:pk>/editar/<int:id>", views.actualizarObra.as_view(), name="actualizarObra"),
    path('<int:pk>/detalle/<int:id>', views.detalleObra.as_view(), name='detalleObra'),
    path("<int:pk>/delete/<int:id>", views.borrarObra.as_view(), name="eliminacion")
]