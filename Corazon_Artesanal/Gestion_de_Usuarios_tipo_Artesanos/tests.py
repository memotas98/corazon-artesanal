from django.test import TestCase, Client
from django.urls import reverse
from .models import Artesano

class GestionDeUsuariosTipoArtesanosTests(TestCase):
    def setUp(self):
        # Crear un Artesano de ejemplo
        self.artesano = Artesano.objects.create(
            nombre='Nombre de prueba',
            telefono='1234567890',
            historia='Historia de prueba',
            fecha_nacimiento='1990-01-01',
            correo_electronico='correo@example.com',
            contraseña='contra'  
        )

        self.client = Client()

    def test_index_view(self):
        response = self.client.get(reverse('Gestion_de_Usuarios_tipo_Artesanos:indexArtesano', kwargs={'pk': self.artesano.pk}))
        self.assertEqual(response.status_code, 200)

    def test_login_view(self):
        login_data = {
        'correo_electronico': 'correo@example.com',
        'contraseña': 'contra'
        }
        response = self.client.post(reverse('Gestion_de_Usuarios_tipo_Artesanos:loginArtesano'), login_data, follow=True)
        self.assertEqual(response.status_code, 200)
