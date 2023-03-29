from django.shortcuts import render, get_object_or_404, redirect
from InscripcionNatacion.models import Usuario, Profesor, Clase
from InscripcionNatacion.forms import CrearUsuarioForm, CrearClaseForm, EditarClaseForm, BuscarUsuarioForm
from django.contrib import messages



# Usuario
def usuarios(request):
    all_usuarios = Usuario.objects.all()
    context = {
        "usuarios": all_usuarios,
        "busqueda_form": BuscarUsuarioForm(),
    }
    return render(request, "InscripcionNatacion/usuarios.html", context=context)




#Usuario que ya fue creado
def crear_usuario(request):
    if request.method == 'POST':
        formulario = CrearUsuarioForm(request.POST)

        if formulario.is_valid():
            info_usuario = formulario.cleaned_data
            save_usuario = Usuario(
                nombre=info_usuario['nombre'],
                nombre_usuario=info_usuario['nombre_usuario'],
                contrasenia=info_usuario['contrasenia'],
                email=info_usuario['email'],
            )
            save_usuario.save()
            return redirect("INUsuarios")

    context ={
        "form_busqueda": BuscarUsuarioForm(),
    }
    return render(request, 'InscripcionNatacion/crear_usuario.html', context)




#Creacion de usuario
def usuario_creado(request, nombre, nombre_usuario, contrasenia, email):
    save_usuario = Usuario(
        nombre=nombre,
        nombre_usuario=nombre_usuario,
        contrasenia=contrasenia,
        email=email
    )
    save_usuario.save()
    context = {
        "nombre_usuario": nombre_usuario,
    }
    return render(request, "InscripcionNatacion/guardar_usuario.html", context)



#Busqueda de usuario
def buscar_usuarios(request):
    usaurio_form = BuscarUsuarioForm(request.get)

    if usaurio_form.is_valid():
        info_usuario = usaurio_form.cleaned_data
        filtra_usuario = Usuario.objects.filter(nombre_usuario__icontains=info_usuario['nombre_usuario'])
        context ={
            "nombre_usuario": filtra_usuario
        }

        return render(request, "InscripcionNatacion/buscar_usuarios.html", context=context)



#Edicion de usuario
def editar_usuario(request, nombre_usuario):
    get_usuario = Usuario.objects.get(nombre_usuario=nombre_usuario)

    if request.method == 'POST':
        usaurio_form = CrearUsuarioForm(request.POST)
        if usaurio_form.is_valid():
            info_usuario = usaurio_form.cleaned_data
            get_usuario.nombre = info_usuario['nombre']
            get_usuario.nombre_usuario = info_usuario['nombre_usuario']
            get_usuario.contrasenia = info_usuario['contrasenia']
            get_usuario.mail = info_usuario['mail']

            get_usuario.save()
            return redirect("INUsuarios")

    context = {
        "nombre_usuario": nombre_usuario,
        "formulario": CrearUsuarioForm(initial={
            "nombre": get_usuario.nombre,
            "nombre_usuario": get_usuario.nombre_usuario,
            "contrasenia": get_usuario.contrasenia,
            "mail": get_usuario.mail
        })
    }

    return redirect(request, "InscripcionNatacion/editar_usuario.html", context=context)




#Eliminacion de usuario
def eliminar_usuario(request, nombre_usuario):
    get_usuario = Usuario.objects.get(nombre_usuario=nombre_usuario)
    get_usuario.delete()

    return redirect("INUsuarios")





# Clases
def clase(request):
    all_clase = Usuario.objects.all()
    context = {
        "clase": all_clase,
        "busqueda_form": BuscarclaseForm(),
    }
    return render(request, "InscripcionNatacion/usuarios.html", context=context)


#Creacion de clase
def crear_clase(request):
    if request.method == 'POST':
        form = CrearClaseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Clase creada exitosamente')
            return redirect('lista_clases')
    else:
        form = CrearClaseForm()
    return render(request, 'InscripcionNatacion/crear_clase.html', {'form': form})



#Lista de clase
def lista_clases(request):
    clases = Clase.objects.all()
    return render(request, 'InscripcionNatacion/lista_clases.html', {'clases': clases})



#Edicion de clase
def editar_clase(request, id):
    clase = get_object_or_404(Clase, id=id)
    if request.method == 'POST':
        form = EditarClaseForm(request.POST, instance=clase)
        if form.is_valid():
            form.save()
            messages.success(request, 'Clase actualizada exitosamente')
            return redirect('lista_clases')
    else:
        form = EditarClaseForm(instance=clase)
    return render(request, 'InscripcionNatacion/editar_clase.html', {'form': form, 'clase': clase})





# Profesores
def lista_profesores(request):


    return render(request, "base.html")

