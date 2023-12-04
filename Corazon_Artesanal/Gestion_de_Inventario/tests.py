from django.test import TestCase
from django.urls import reverse
from .models import Obra
from Gestion_de_Usuarios_tipo_Artesanos.models import Artesano
from datetime import date  

class GestionDeInventarioTests(TestCase):

    def setUp(self):
        self.artesano = Artesano.objects.create(
            fecha_nacimiento=date(1998, 1, 1),
            contraseña='contra',
            nombre='Artista Prueba',
            telefono='1234567890',
            historia='Historia de prueba',
            correo_electronico='prueba@example.com'
        )
        self.obra = Obra.objects.create(
            id_artesano=self.artesano,
            nombre='Obra de Prueba',
            precio=100,
            descripcion='Una obra de prueba',
            proceso_creativo='Proceso creativo de prueba',
            cantidadExistente=5
        )

    def test_crear_obra_view_post(self):
        data = {
            'nombre': 'Nueva Obra',
            'precio': 150,
            'descripcion': 'Descripción de la nueva obra',
            'proceso_creativo': 'Proceso creativo de la nueva obra',
            'cantidadExistente': 10
        }
        response = self.client.post(reverse('Gestion_de_Inventario:agregarObra', kwargs={'pk': self.artesano.pk}), data)
        self.assertEqual(response.status_code, 302)  # Debería redirigir después de un POST
        self.assertTrue(Obra.objects.filter(nombre='Nueva Obra').exists())

    def test_actualizar_obra_view_post(self):
        data = {
            'nombre': 'Obra Actualizada',
            'precio': 200,
            'descripcion': 'Nueva descripción',
            'proceso_creativo': 'Nuevo proceso creativo',
            'cantidadExistente': 8
        }
        response = self.client.post(reverse('Gestion_de_Inventario:actualizarObra', kwargs={'pk': self.artesano.pk, 'id': self.obra.pk}), data)
        self.assertEqual(response.status_code, 302)  # Debería redirigir después de un POST
        self.obra.refresh_from_db()
        self.assertEqual(self.obra.nombre, 'Obra Actualizada')
