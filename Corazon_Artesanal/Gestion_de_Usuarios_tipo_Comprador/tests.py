from django.test import TestCase, Client
from django.urls import reverse
from .models import Comprador

class GestionDeUsuariosTipoCompradorTests(TestCase):
    def setUp(self):
        # Crear un Artesano de ejemplo
        self.comprador = Comprador.objects.create(
            username="prueba_1",
            first_name='Nombre de prueba',
            last_name='last name',
            telefono='1234567890',
            direccion='Historia de prueba',
            fecha_nacimiento='1990-01-01',
            email='correo@example.com',
            password='contra'  
        )

        self.client = Client()

    def test_index_view(self):
        response = self.client.get(reverse('Gestion_de_Usuarios_tipo_Comprador:indexComprador', kwargs={'pk': self.comprador.pk}))
        self.assertEqual(response.status_code, 200)

    def test_login_view(self):
        login_data = {
        'username': 'prueba_1',
        'password': 'contra'
        }
        response = self.client.post(reverse('Gestion_de_Usuarios_tipo_Comprador:loginComprador'), login_data, follow=True)
        self.assertEqual(response.status_code, 200)
