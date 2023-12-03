from django.urls import path
from . import views

app_name = "Gestion_de_Usuarios_tipo_Artesanos"
urlpatterns = [
    path('index/<int:pk>', views.IndexView, name='indexArtesano'),
    path('login/', views.LoginView, name='loginArtesano'),
    path("perfil/<int:pk>/", views.PerfilArtesano.as_view(), name="perfilArtesano"),
    path('', views.RegistroView.as_view(), name='RegistroArtesano')
]