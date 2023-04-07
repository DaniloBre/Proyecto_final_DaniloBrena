from django.db import models

# Create your models here.




#opciones de Personas
personas = [
    [0, 'Mi persona'],
    [1, 'Mi pareja'],
    [2, 'Mi hijo/hija'],
    [3, 'Otros'],
]

genero =[
    [0, 'Hombre'],
    [1, 'Mujer'],
    [2, 'Otros'],
]

#Modelo usuario
class DatosPersona(models.Model):
    persona = models.IntegerField(choices=personas)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30, unique=True)
    edad = models.IntegerField()
    email = models.EmailField()
    genero = models.IntegerField(choices=genero)
    numero_documento = models.IntegerField()

    def __str__(self):
        return f"Datos de la persona: {self.nombre} ({self.apellido})"





#opciones de Clases
niveles = [
    [0, 'Nuevo en la actividad'],
    [1, 'Poco conocimiento'],
    [2, 'Bueno en la actividad'],
    [3, 'Avansado'],
    [4, 'Desconosco']
]

dias = [
    [0, "Lunes"],
    [1, "Martes"],
    [2, "Miercoles"],
    [3, "Jueves"],
    [4, "Viernes"],
    [5, "Sabado"],
]

horarios = [
    [0, '10'],
    [1, '11'],
    [2, '13'],
    [3, '14'],
    [4, '15'],
    [5, '16'],
    [6, '17'],
    [7, '18'],
    [8, '19'],
    [9, '20'],
]


#Modelo elecion de nivel, dia y horario
class Clase(models.Model):
    nivel = models.IntegerField(choices=niveles)
    dia = models.IntegerField(choices=dias, unique=True)
    horario = models.IntegerField(choices=horarios)
    incapacidad = models.BooleanField(default=False)

    def __str__(self):
        return f"Clase: {self.dia} a las {self.horario}"







profe_nombre = [
    [0, 'Juan Topo'],
    [1, 'Tomas Ramirez'],
    [2, 'Maximo Decimo Meridio'],
]


#Modelo elecion de profesor
class Profesor(models.Model):
    nombre_profe = models.IntegerField(choices=profe_nombre, unique=True)
    email_profe = models.EmailField()

    def save(self, *args, **kwargs):
        if self.nombre_profe == 0:
            self.email_profe = "juantopo32@gmail.com"

        elif self.nombre_profe == 1:
            self.email_profe = "tomasramirez12@gmail.com"

        elif self.nombre_profe == 2:
            self.email_profe = "maximeri10@gmail.com"

        super().save(*args, **kwargs)


    def __str__(self):
        return f"Profesor: {self.nombre_profe}"







coemtario_tipo = [
    [0, 'Pocitivo'],
    [1, 'Neutral'],
    [2, 'Negativo'],
]


#Comenta area
class Comentario(models.Model):
    nombre_comenta = models.CharField(max_length=30, unique=True)
    email_comenta = models.EmailField()
    tipo_coemtario = models.IntegerField(choices=coemtario_tipo)
    mensaje = models.TextField()

    def __str__(self):
        return f"Nombre de la persona que comenta: {self.nombre_comenta}"