from django.db import models

# Create your models here.




#Modelo usuario
class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    nombre_usuario = models.CharField(max_length=30)
    contrasenia = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f"Usuario: {self.nombre} ({self.nombre_usuario})"



#Modelo elecion de dia y horario
class Clase(models.Model):
    Elecion_Dia = (
        ('L', 'Lunes'),
        ('M', 'Martes'),
        ('X', 'Miércoles'),
        ('J', 'Jueves'),
        ('V', 'Viernes'),
        ('S', 'Sábado'),
    )

    Elechion_Hs = (
        ('10:00', '10:00'),
        ('11:00', '11:00'),
        ('12:00', '12:00'),
        ('13:00', '13:00'),
        ('14:00', '14:00'),
        ('15:00', '15:00'),
        ('16:00', '16:00'),
        ('17:00', '17:00'),
        ('18:00', '18:00'),
        ('19:00', '19:00'),
    )

    dia = models.CharField(max_length=1, choices=Elecion_Dia)
    horario = models.CharField(max_length=5, choices=Elechion_Hs)

    def __str__(self):
        return f"Clase: {self.get_dia_display()} a las {self.horario}"




#Modelo elecion de profesor
class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)


    def __str__(self):
        return f"Profesor: {self.nombre} {self.apellido}"

