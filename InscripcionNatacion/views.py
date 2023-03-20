from django.shortcuts import render, get_object_or_404, redirect
from InscripcionNatacion.models import Usuario, Profesor, Clase
from InscripcionNatacion.forms import CrearUsuarioForm, EditarUsuarioForm, CrearClaseForm, EditarClaseForm, BuscarUsuarioForm
from django.contrib import messages



# Usuario
def usuarios(request):
    all_usuario = Usuario.objects.all()
    context = {
        "usuario": all_usuario,
        "form_busqueda": BuscarUsuarioForm(),
    }
    return render(request, "AppCoder/cursos.html", context=context)


#Creacion de usuario
def crear_usuario(request):
    if request.method == 'POST':
        form = CrearUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario creado exitosamente')
            return redirect('listar_usuarios')
    else:
        form = CrearUsuarioForm()
    return render(request, 'InscripcionNatacion/crear_usuario.html', {'form': form})



#Lista de usuario
def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'InscripcionNatacion/listar_usuarios.html', {'usuarios': usuarios})



#Busqueda de usuario
def buscar_usuarios(request):
    query = request.GET.get('q')
    if query:
        usuarios = Usuario.objects.filter(username__icontains=query)
        return render(request, 'InscripcionNatacion/listar_usuarios.html', {'usuarios': usuarios})
    else:
        return redirect('listar_usuarios')



#Edicion de usuario
def editar_usuario(request, nombre_usuario):
    usuario = get_object_or_404(Usuario, username=nombre_usuario)
    if request.method == 'POST':
        form = EditarUsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario actualizado exitosamente')
            return redirect('listar_usuarios')
    else:
        form = EditarUsuarioForm(instance=usuario)
    return render(request, 'InscripcionNatacion/editar_usuario.html', {'form': form, 'usuario': usuario})



#Eliminacion de usuario
def eliminar_usuario(request, nombre_usuario):
    usuario = get_object_or_404(Usuario, username=nombre_usuario)
    if request.method == 'POST':
        usuario.delete()
        messages.success(request, 'Usuario eliminado exitosamente')
        return redirect('listar_usuarios')
    return render(request, 'InscripcionNatacion/eliminar_usuario.html', {'usuario': usuario})





# Clases

#Creacion de clase
def crear_clase(request):
    if request.method == 'POST':
        form = CrearClaseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Clase creada exitosamente')
            return redirect('listar_clases')
    else:
        form = CrearClaseForm()
    return render(request, 'InscripcionNatacion/crear_clase.html', {'form': form})



#Lista de clase
def lista_clases(request):
    clases = Clase.objects.all()
    return render(request, 'InscripcionNatacion/listar_clases.html', {'clases': clases})



#Edicion de clase
def editar_clase(request, id):
    clase = get_object_or_404(Clase, id=id)
    if request.method == 'POST':
        form = EditarClaseForm(request.POST, instance=clase)
        if form.is_valid():
            form.save()
            messages.success(request, 'Clase actualizada exitosamente')
            return redirect('listar_clases')
    else:
        form = EditarClaseForm(instance=clase)
    return render(request, 'InscripcionNatacion/editar_clase.html', {'form': form, 'clase': clase})





# Profesores
def lista_profesores(request):
    profesores = Profesor.objects.all()
    return render

