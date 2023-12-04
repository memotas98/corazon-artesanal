from django.test import TestCase, Client
from django.urls import reverse
from .models import Obra
from Gestion_de_Usuarios_tipo_Artesanos.models import Artesano

class GestionDeProductosTests(TestCase):
    def setUp(self):
        # Crear un Artesano de ejemplo
        self.artesano = Artesano.objects.create(
            fecha_nacimiento='1990-01-01',
            contraseña='contra',
            nombre='Nombre del Artesano',
            telefono='1234567890',
            historia='Historia de prueba',
            correo_electronico='correo@example.com'
        )

        # Crear una Obra de ejemplo
        self.obra = Obra.objects.create(
            id_artesano=self.artesano,
            nombre='Obra de prueba',
            precio=100,
            descripcion='Descripción de prueba',
            proceso_creativo='Proceso creativo de prueba',
            cantidadExistente=5
        )

        self.client = Client()

    def test_catalogo_view(self):
        response = self.client.get(reverse('Gestion_de_Productos:catalogo', kwargs={'pk': self.artesano.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.obra.nombre)

    def test_detalle_obra_view(self):
        response = self.client.get(reverse('Gestion_de_Productos:detalleObra', kwargs={'pk': self.artesano.pk, 'id': self.obra.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.obra.nombre)
