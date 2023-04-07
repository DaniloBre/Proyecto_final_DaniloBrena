from django.contrib import admin
from InscripcionNatacion.models import DatosPersona, Clase, Profesor, Comentario


# Register your models here.

admin.site.register(DatosPersona)
admin.site.register(Clase)
admin.site.register(Profesor)
admin.site.register(Comentario)