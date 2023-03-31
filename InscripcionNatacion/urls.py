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
    path('clase', clases, name='INClases'),
    path('clase/crear', crear_clase, name='INCrearClase'),
    path('clase/<dia>/<horario>/', clase_creada, name='INClaseCreada'),
    path('buscar_clase', buscar_clase, name='INBuscarCreada'),
    path('clase/editar/<dia>/', editar_usuario, name='INEditarClase'),
    path('clase/eliminar/<dia>/', eliminar_clase, name='INEliminarClase'),


    #Profesores
    path('profesor', profesores, name='INProfesores'),
    path('profesor/crear', crear_clase, name='INCrearProfesor'),
    path('profesor/<nombre_profe>/<apellido_profe>/', clase_creada, name='INProfesorCreada'),
    path('buscar_clase', buscar_clase, name='INBuscarProfesor'),
    path('profesor/editar/<nombre_profe>/', editar_usuario, name='INEditarProfesor'),
    path('profesor/eliminar/<nombre_profe>/', eliminar_clase, name='INEliminarProfesor'),

]
