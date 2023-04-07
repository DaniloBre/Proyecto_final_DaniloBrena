from django.urls import path
from InscripcionNatacion.views import *


urlpatterns = [
    #Usuario
    path('personas', personas, name='INPersonas'),
    path('personas/crear', crear_persona, name='INCrearPersona'),
    path('personas/<persona>/<nombre>/<apellido>/<edad>/<email>/<numero_documento>', persona_creado, name='INPersonaCrear'),
    path('buscar_usuarios', buscar_persona, name='INBuscarPersonas'),
    path('personas/editar/<apellido>', editar_persona, name='INEditarPersona'),
    path('personas/eliminar/<apellido>', eliminar_persona, name='INEliminarPersona'),


    #Clase
    path('clases', clases, name='INClases'),
    path('clases/crear', crear_clase, name='INCrearClase'),
    path('clases/<nivel>/<dia>/<horario>/<incapacidad>/', clase_creada, name='INClaseCreada'),
    path('buscar_clases', buscar_clase, name='INBuscarClase'),
    path('clases/editar/<dia>/', editar_clase, name='INEditarClase'),
    path('clases/eliminar/<dia>/', eliminar_clase, name='INEliminarClase'),


    #Profesores
    path('profesors', profesores, name='INProfesores'),
    path('profesors/crear', crear_profesor, name='INCrearProfesor'),
    path('profesors/<nombre_profe>/<email_profe>/', profesor_creada, name='INProfesorCreada'),
    path('buscar_clases', buscar_profesor, name='INBuscarProfesor'),
    path('profesors/editar/<nombre_profe>/', editar_profesor, name='INEditarProfesor'),
    path('profesors/eliminar/<nombre_profe>/', eliminar_profesor, name='INEliminarProfesor'),


    #Comentario
    path('comentarios', comentarios, name='INComentarios'),
    path('comentarios/crear', crear_comentario, name='INCrearComentarios'),
    path('comentarios/<nombre_comenta>/<email_comenta>/<tipo_coemtario>/<mensaje>/', comentario_creado, name='INComentariosCreada'),
    path('buscar_comentario', buscar_comentario, name='INBuscarComentarios'),
]
