from django.urls import path
from InscripcionNatacion.views import *


urlpatterns = [
    #Usuario
    path('usuarios', usuarios, name='INUsuarios'),
    path('usuarios/crear', crear_usuario, name='INCrearUsuario'),
    path('usuarios/<nombre>/<nombre_usuario>/<contrasenia>/<email>', usuario_creado, name='INUsuarioCrear'),
    path('buscar_usuarios', buscar_usuarios, name='INBuscarUsuarios'),
    path('usuarios/editar/<nombre_usuario>', editar_usuario, name='INEditarUsuario'),
    path('usuarios/eliminar/<nombre_usuario>', eliminar_usuario, name='INEliminarUsuario'),


    #Clase
    path('clases', clases, name='INClases'),
    path('clases/crear', crear_clase, name='INCrearClase'),
    path('clases/<dia>/<horario>/', clase_creada, name='INClaseCreada'),
    path('buscar_clases', buscar_clase, name='INBuscarCreada'),
    path('clases/editar/<dia>/', editar_usuario, name='INEditarClase'),
    path('clases/eliminar/<dia>/', eliminar_clase, name='INEliminarClase'),


    #Profesores
    path('profesors', profesores, name='INProfesores'),
    path('profesors/crear', crear_profesor, name='INCrearProfesor'),
    path('profesors/<nombre_profe>/<apellido_profe>/', profesor_creada, name='INProfesorCreada'),
    path('buscar_clases', buscar_profesor, name='INBuscarProfesor'),
    path('profesors/editar/<nombre_profe>/', editar_profesor, name='INEditarProfesor'),
    path('profesors/eliminar/<nombre_profe>/', eliminar_profesor, name='INEliminarProfesor'),

]
