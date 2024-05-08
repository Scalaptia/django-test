# from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.
class PruebasPaginaDeInicio(SimpleTestCase):
    def test_la_url_existe_en_la_ubicacion_correcta(self):
        respuesta = self.client.get('/')
        self.assertEqual(respuesta.status_code, 200)

    def test_url_disponible_por_nombre(self):
        respuesta = self.client.get(reverse('inicio'))
        self.assertEqual(respuesta.status_code, 200)

    def test_nombre_correecto_de_la_plantilla(self):
        respuesta = self.client.get(reverse('inicio'))
        self.assertTemplateUsed(respuesta, "inicio.html")

    def test_contenido_de_la_plantilla(self):
        respuesta = self.client.get(reverse('inicio'))
        self.assertContains(respuesta, "<h1>Página de inicio</h1>")
        

class PruebasPaginaAcercaDe(SimpleTestCase):
    def test_la_url_existe_en_la_ubicacion_correcta(self):
        respuesta = self.client.get('/about/')
        self.assertEqual(respuesta.status_code, 200)

    def test_url_disponible_por_nombre(self):
        respuesta = self.client.get(reverse('about'))
        self.assertEqual(respuesta.status_code, 200)

    def test_nombre_correecto_de_la_plantilla(self):
        respuesta = self.client.get(reverse('about'))
        self.assertTemplateUsed(respuesta, "about.html")

    def test_contenido_de_la_plantilla(self):
        respuesta = self.client.get(reverse('about'))
        self.assertContains(respuesta, "<h1>Página acerca de</h1>")