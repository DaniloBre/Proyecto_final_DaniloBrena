from django.test import TestCase
from django.urls import reverse

from InscripcionNatacion import PrimerosDatos, Clase, Profesor, Comentario

# Create your tests here.



class PrimerosDatosTestCase(TestCase):
    def setUp(self):
        PrimerosDatos.objects.create(
            persona=[1],
            nombre="Dani",
            apellido="Bre",
            edad=23,
            email="danilo.brena@gmail.com",
            numero_documento=12345678
        )
        PrimerosDatos.objects.create(
            persona=[4],
            nombre="Ezeq",
            apellido="Rami",
            edad=35,
            email="ezerami@gmail.com",
            numero_documento=87654321
        )


    def test_creando_persona(self):
        d1 = PrimerosDatos.objects.get(apellido="Bre")
        e1 = PrimerosDatos.objects.get(apellido="Rami")
        self.assertEquals(d1.nombre, "Dani")
        self.assertEquals(e1.nombre, "Ezeq")


class ViewTestsPersona(TestCase):
    def test_pregunta_persona(self):
        response = self.client.get(reverse('INPersonas'))
        self.assertEquals(response.status_code, 200)
        self.assertContains(reverse('Creacion de persona'))

    def test_pasa_pregunta_persona(self):
        persona = PrimerosDatos.objects.create(nombre="Dani", apellido="Bre")
        response = self.client.get(reverse('INPersonas'))
        self.assertEquals(response.status_code, 200)
        self.assertContains(
            response,
            f"Nombre: Dani - Apellido: Bre"
        )



class ClaseTestCase(TestCase):
    def setUp(self):
        Clase.objects.create(
            nivel=[4],
            dia=[3],
            horario=[9],
            incapacidad=False
        )
        Clase.objects.create(
            nivel=[1],
            dia=[2],
            horario=[4],
            incapacidad=True
        )

    def test_creando_clase(self):
        di1 = Clase.objects.get(dia=[3])
        di2 = Clase.objects.get(dia=[2])
        self.assertEquals(di1.horario, [9])
        self.assertEquals(di2.horario, [4])



class ViewTestsClase(TestCase):
    def test_pregunta_clase(self):
        response = self.client.get(reverse('INClases'))
        self.assertEquals(response.status_code, 200)
        self.assertContains(reverse('Creacion de clases'))

    def test_pasa_pregunta_clase(self):
        clase = Clase.objects.create(dia=[3], horario=[9])
        response = self.client.get(reverse('INClases'))
        self.assertEquals(response.status_code, 200)
        self.assertContains(
            response,
            f"Dia: Miercoles - Horario: 20 hs"
        )




class ProfesorTestCase(TestCase):
    def setUp(self):
        Profesor.objects.create(nombre_profe=[4], email_profe=(),)
        Profesor.objects.create(nombre_profe=[1], email_profe=(),)

    def test_creando_clase(self):
        prof1 = Profesor.objects.get(nombre_profe=[3])
        prof2 = Profesor.objects.get(nombre_profe=[2])
        self.assertEquals(prof1.horario, [9])
        self.assertEquals(prof2.horario, [4])



class ViewTestsProfesor(TestCase):
    def test_pregunta_clase(self):
        response = self.client.get(reverse('INProfesores'))
        self.assertEquals(response.status_code, 200)
        self.assertContains(reverse('Elecion de profesor'))

    def test_pasa_pregunta_clase(self):
        profesor = Profesor.objects.create(nombre_profe=[3], email_profe=())
        response = self.client.get(reverse('INProfesores'))
        self.assertEquals(response.status_code, 200)
        self.assertContains(
            response,
            f"Profesor: Juan Topo - Email: juantopo32@gmail.com"
        )





class ComentarioTestCase(TestCase):
    def setUp(self):
        Comentario.objects.create(
            nombre_comenta="Dani Bre",
            email_comenta="danilo.brena@gmail.com",
            tipo_coemtario=[2],
            mensaje="Esta bien"
        )
        Comentario.objects.create(
            nombre_comenta="Ezeq Rami",
            email_comenta="ezerami@gmail.com",
            tipo_coemtario=[1],
            mensaje="Faltan cosas"
        )

    def test_creando_clase(self):
        comen1 = Comentario.objects.get(nombre_comenta="Dani Bre")
        comen2 = Comentario.objects.get(nombre_comenta="Ezeq Rami")
        self.assertEquals(comen1.email_comenta, "danilo.brena@gmail.com")
        self.assertEquals(comen2.email_comenta, "ezerami@gmail.com")



class ViewTestsComentario(TestCase):
    def test_pregunta_clase(self):
        response = self.client.get(reverse('INComentarios'))
        self.assertEquals(response.status_code, 200)
        self.assertContains(reverse('Comentarios'))

    def test_pasa_pregunta_clase(self):
        profesor = Comentario.objects.create(nombre_comenta="Dani Bre", mensaje="Esta bien")
        response = self.client.get(reverse('INComentarios'))
        self.assertEquals(response.status_code, 200)
        self.assertContains(
            response,
            f"Autor del comentario: Dani Bre - Mensaje: Esta bien"
        )

