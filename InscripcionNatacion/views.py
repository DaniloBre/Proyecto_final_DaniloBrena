from django.shortcuts import render, redirect
from InscripcionNatacion.models import Usuario, Profesor, Clase
from InscripcionNatacion.forms import (CrearUsuarioForm, CrearClaseForm, CrearProfesorForm,
                                       BuscarUsuarioForm, BuscarClaseForm, BuscarProfesorForm,
                                       )



# Usuario
def usuarios(request):
    all_usuarios = Usuario.objects.all()
    context = {
        "usuarios": all_usuarios,
        "busqueda_form_usuario": BuscarUsuarioForm(),
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
        "form_usuario": CrearUsuarioForm(),
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
            get_usuario.email = info_usuario['email']

            get_usuario.save()
            return redirect("INUsuarios")

    context = {
        "nombre_usuario": nombre_usuario,
        "form_edit_usuario": CrearUsuarioForm(initial={
            "nombre": get_usuario.nombre,
            "nombre_usuario": get_usuario.nombre_usuario,
            "contrasenia": get_usuario.contrasenia,
            "email": get_usuario.email
        })
    }

    return render(request, "InscripcionNatacion/editar_usuario.html", context=context)



#Eliminacion de usuario
def eliminar_usuario(request, nombre_usuario):
    get_usuario = Usuario.objects.get(nombre_usuario=nombre_usuario)
    get_usuario.delete()

    return redirect("INUsuarios")







# Clases
def clases(request):
    all_clase = Clase.objects.all()
    context = {
        "clase": all_clase,
        "busqueda_form_clase": BuscarClaseForm(),
    }
    return render(request, "InscripcionNatacion/usuarios.html", context=context)



#Clase que ya fue creado
def crear_clase(request):
    if request.method == 'POST':
        form_clas = CrearClaseForm(request.POST)

        if form_clas.is_valid():
            info_clase = form_clas.cleaned_data
            save_clase = Clase(
                dia=info_clase['dia'],
                horario=info_clase['horario'],
            )
            save_clase.save()
            return redirect('INUsuarios')

    context ={
        "form_clase": CrearClaseForm(),
    }

    return render(request, 'InscripcionNatacion/crear_clase.html', context=context)



#Creacion de clase
def clase_creada(request, dia, horario):
    save_clase = Clase(
        dia=dia,
        horario=horario,
    )
    save_clase.save()
    context = {
        "dia": dia,
    }
    return render(request, "InscripcionNatacion/guardar_clase.html", context)



#Busqueda de clase
def buscar_clase(request):
    clase_form = BuscarClaseForm(request.get)

    if clase_form.is_valid():
        info_clase = clase_form.cleaned_data
        filtra_clase = Clase.objects.filter(dia__icontains=info_clase['dia'])
        context ={
            "dia": filtra_clase
        }

        return render(request, "InscripcionNatacion/buscar_usuarios.html", context=context)



#Edicion de clase
def editar_clase(request, dia):
    get_clase = Clase.objects.get(dia=dia)

    if request.method == 'POST':
        clase_form = CrearClaseForm(request.POST)

        if clase_form.is_valid():
            info_clase = clase_form.cleaned_data

            get_clase.dia = info_clase['dia']
            get_clase.horario = info_clase['horario']

            get_clase.save()
            return redirect('INUsuarios')

    context ={
        "dia": dia,
        "form_edit_clase": CrearClaseForm(initial={
            "dia": get_clase.dia,
            "horario": get_clase.horario
        })
    }

    return render(request, 'InscripcionNatacion/editar_clase.html', context=context)



#Eliminar clase
def eliminar_clase (request, dia):
    get_clase = Clase.objects.get(dia=dia)
    get_clase.delete()

    return redirect("INUsuarios")







# Profesores
def profesores(request):
    all_profesores = Profesor.objects.all()
    context = {
        "profesores": all_profesores,
        "busqueda_form_profe": BuscarProfesorForm(),
    }

    return render(request, "InscripcionNatacion/usuarios.html", context=context)



#Profesor que ya fue creado
def crear_profesor(request):
    if request.method == 'POST':
        form_profe = CrearProfesorForm(request.POST)

        if form_profe.is_valid():
            info_profe = form_profe.cleaned_data
            save_profe = Clase(
                nombre_profe=info_profe['nombre_profe'],
                apellido_profe=info_profe['apellido_profe'],
            )
            save_profe.save()
            return redirect('INUsuarios')

    context = {
        "form_profesor": CrearProfesorForm(),
    }

    return render(request,'InscripcionNatacion/crear_profesor.html', context=context)



#Profesor de clase
def profesor_creada(request, nombre_profe, apellido_profe):
    save_profe = Profesor(
        nombre_profe=nombre_profe,
        apellido_profe=apellido_profe,
    )
    save_profe.save()
    context = {
        "nombre_profe": nombre_profe,
    }
    return render(request, "InscripcionNatacion/guardar_profesor.html", context)



#Busqueda de profesor
def buscar_profesor(request):
    profe_form = BuscarProfesorForm(request.get)

    if profe_form.is_valid():
        info_profe = profe_form.cleaned_data
        filtra_profe = Clase.objects.filter(nombre_profe__icontains=info_profe['nombre_profe'])
        context ={
            "nombre_profe": filtra_profe
        }

        return render(request, "InscripcionNatacion/buscar_usuarios.html", context=context)



#Edicion de profesor
def editar_profesor(request, nombre_profe):
    get_profesor = Profesor.objects.get(nombre_profe=nombre_profe)

    if request.method == 'POST':
        clase_form = CrearClaseForm(request.POST)

        if clase_form.is_valid():
            info_profe = clase_form.cleaned_data

            get_profesor.nombre_profe = info_profe['nombre_profe']
            get_profesor.apellido_profe = info_profe['apellido_profe']

            get_profesor.save()
            return redirect('INUsuarios')

    context ={
        "nombre_profe": nombre_profe,
        "form_edit_profe": CrearClaseForm(initial={
            "nombre_profe": get_profesor.nombre_profe,
            "apellido_profe": get_profesor.apellido_profe
        })
    }

    return render(request, 'InscripcionNatacion/editar_profesor.html', context=context)



#Eliminar profesor
def eliminar_profesor (request, nombre_profe):
    get_profe = Profesor.objects.get(nombre_profe=nombre_profe)
    get_profe.delete()

    return redirect("INUsuarios")






