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
    path('clase/crear/', crear_clase, name='INCrearClase'),
    path('clase/', lista_clases, name='INListarClases'),
    path('clase/editar/<id>/', editar_usuario, name='INEditarClase'),

    #Profesores
    path('profesor/', lista_profesores, name='INListarProfesores'),

]
