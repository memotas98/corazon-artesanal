from django.urls import path
from . import views

app_name = "Gestion_de_Usuarios_tipo_Comprador"
urlpatterns = [
    path('index/<int:pk>', views.IndexView, name='indexComprador'),
    path('login/', views.LoginView, name='loginComprador'),
    path("perfil/<int:pk>/", views.PerfilComprador.as_view(), name="perfilComprador"),
    path('<int:pk>/detalle/autor/<int:id>', views.detalleAutor.as_view(), name="detalleAutor"),
    path('', views.RegistroView, name='RegistroComprador')
]

