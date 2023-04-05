from django.test import TestCase
from django.urls import reverse

from InscripcionNatacion import Usuario

# Create your tests here.


class UsuarioTestCase(TestCase):
    def setUp(self):
        Usuario.objects.create(nombre="Dani", nombre_usuario="Dan1")
        Usuario.objects.create(nombre="Ezeq", nombre_usuario="Eze1")


    def test_creando_usuario(self):
        d1 = Usuario.objects.get(nombre_usuario="Dan1")
        e1 = Usuario.objects.get(nombre_usuario="Eze1")
        self.assertEquals(d1.nombre, "Dani")
        self.assertEquals(e1.nombre, "Ezeq")


class ViewTests(TestCase):
    def test_pregunta(self):
        response = self.client.get(reverse('INUsuario'))
        self.assertEquals(response.status_code, 200)
        self.assertContains(reverse('Creacion de usuario'))

    def test_pasa_pregunta(self):
        usuario = Usuario.objects.create(nombre="Dani", nombre_usuario="Dan1")
        response = self.client.get(reverse('INUsuario'))
        self.assertEquals(response.status_code, 200)
        self.assertContains(
            response,
            f"Nombre: Dani - Nombre de usuario: Dan1"
        )



