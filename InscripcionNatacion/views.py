

from django.shortcuts import render, redirect
from InscripcionNatacion.models import DatosPersona, Profesor, Clase, Comentario
from InscripcionNatacion.forms import (CrearPersonaForm, CrearClaseForm, CrearProfesorForm, CrearComentarioForm,
                                       BuscarPersonaForm, BuscarClaseForm, BuscarProfesorForm, BuscarComentarioForm
                                       )



# Usuario
def personas(request):
    all_personas = DatosPersona.objects.all()
    context = {
        "personas": all_personas,
        "busqueda_form_personas": BuscarPersonaForm(),
    }
    return render(request, "InscripcionNatacion/personas.html", context=context)



#Persona que ya fue creado
def crear_persona(request):
    if request.method == 'POST':
        formulario = CrearPersonaForm(request.POST)

        if formulario.is_valid():
            info_persona = formulario.cleaned_data
            save_persona = DatosPersona(
                persona=info_persona['persona'],
                nombre=info_persona['nombre'],
                apellido=info_persona['apellido'],
                edad=info_persona['edad'],
                email=info_persona['email'],
                genero=info_persona['genero'],
                numero_documento=info_persona['numero_documento']
            )
            save_persona.save()
            return redirect("INPersonas")

    context = {
        "form_persona": CrearPersonaForm(),
    }
    return render(request, 'InscripcionNatacion/crear_usuario.html', context)



#Creacion de persona
def persona_creado(request, persona, nombre, apellido, edad, email, genero, numero_documento):
    save_persona = DatosPersona(
        persona=persona,
        nombre=nombre,
        apellido=apellido,
        edad=edad,
        email=email,
        genero=genero,
        numero_documento=numero_documento
    )
    save_persona.save()
    context = {
        "apellido": apellido,
    }
    return render(request, "InscripcionNatacion/guardar_usuario.html", context)



#Busqueda de usuario
def buscar_persona(request):
    persona_form = BuscarPersonaForm(request.GET)

    if persona_form.is_valid():
        info_persona = persona_form.cleaned_data
        filtra_persona = DatosPersona.objects.filter(apellido__icontains=info_persona['apellido'])
        context ={
            "apellido": filtra_persona
        }

        return render(request, "InscripcionNatacion/buscar_usuarios.html", context=context)



#Edicion de usuario
def editar_persona(request, apellido):
    get_persona = DatosPersona.objects.get(apellido=apellido)

    if request.method == 'POST':

        info_persona = request.POST
        print(info_persona)
        get_persona.persona = info_persona['persona']
        get_persona.nombre = info_persona['nombre']
        get_persona.apellido = info_persona['apellido']
        get_persona.email = info_persona['email']
        get_persona.genero = info_persona['genero']
        get_persona.numero_documento = info_persona['numero_documento']

        get_persona.save()
        return redirect("INPersonas")

    context = {
        "apellido": apellido,
        "form_edit_personas": CrearPersonaForm(initial={
            "persona": get_persona.persona,
            "nombre": get_persona.nombre,
            "apellido": get_persona.apellido,
            "email": get_persona.email,
            "genero": get_persona.genero,
            "numero_documento": get_persona.numero_documento
        })
    }

    return render(request, "InscripcionNatacion/editar_usuario.html", context=context)



#Eliminacion de usuario
def eliminar_persona(request, apellido):
    get_persona = DatosPersona.objects.get(apellido=apellido)
    get_persona.delete()

    return redirect("INPersonas")







# Clases
def clases(request):
    all_clase = Clase.objects.all()
    context = {
        "clases": all_clase,
        "busqueda_form_clase": BuscarClaseForm(),
    }
    return render(request, "InscripcionNatacion/personas.html", context=context)



#Clase que ya fue creado
def crear_clase(request):
    if request.method == 'POST':
        form_clas = CrearClaseForm(request.POST)

        if form_clas.is_valid():
            info_clase = form_clas.cleaned_data
            save_clase = Clase(
                nivel=info_clase['nivel'],
                dia=info_clase['dia'],
                horario=info_clase['horario'],
            )
            save_clase.save()
            return redirect('INPersonas')

    context ={
        "form_clase": CrearClaseForm(),
    }

    return render(request, 'InscripcionNatacion/crear_clase.html', context=context)



#Creacion de clase
def clase_creada(request,nivel , dia, horario):
    save_clase = Clase(
        nivel=nivel,
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
    clase_form = BuscarClaseForm(request.GET)

    if clase_form.is_valid():
        info_clase = clase_form.cleaned_data
        filtra_clase = Clase.objects.filter(dia__icontains=info_clase['dia'])
        context ={
            "dia": filtra_clase
        }

        return render(request, "InscripcionNatacion/buscar_clase.html", context=context)



#Edicion de clase
def editar_clase(request, dia):
    get_clase = Clase.objects.get(dia=dia)

    if request.method == 'POST':

        info_clase = request.POST
        print(info_clase)
        get_clase.nivel = info_clase['nivel']
        get_clase.dia = info_clase['dia']
        get_clase.horario = info_clase['horario']

        get_clase.save()
        return redirect('INPersonas')

    context ={
        "dia": dia,
        "form_edit_clase": CrearClaseForm(initial={
            "nivel": get_clase.nivel,
            "dia": get_clase.dia,
            "horario": get_clase.horario
        })
    }

    return render(request, 'InscripcionNatacion/editar_clase.html', context=context)



#Eliminar clase
def eliminar_clase (request, dia):
    get_clase = Clase.objects.get(dia=dia)
    get_clase.delete()

    return redirect("INPersonas")







# Profesores
def profesores(request):
    all_profesores = Profesor.objects.all()
    context = {
        "profesores": all_profesores,
        "busqueda_form_profe": BuscarProfesorForm(),
    }

    return render(request, "InscripcionNatacion/personas.html", context=context)



#Profesor que ya fue creado
def crear_profesor(request):
    if request.method == 'POST':
        form_profe = CrearProfesorForm(request.POST)

        if form_profe.is_valid():
            info_profe = form_profe.cleaned_data
            save_profe = Profesor(
                nombre_profe=info_profe['nombre_profe'],
                email_profe=info_profe['email_profe'],
            )
            save_profe.save()
            return redirect('INPersonas')

    context = {
        "form_profesor": CrearProfesorForm(),
    }

    return render(request,'InscripcionNatacion/crear_profesor.html', context=context)



#Profesor de clase
def profesor_creada(request, nombre_profe, email_profe):
    save_profe = Profesor(
        nombre_profe=nombre_profe,
        email_profe=email_profe,
    )
    save_profe.save()
    context = {
        "nombre_profe": nombre_profe,
    }
    return render(request, "InscripcionNatacion/guardar_profesor.html", context)



#Busqueda de profesor
def buscar_profesor(request):
    profe_form = BuscarProfesorForm(request.GET)

    if profe_form.is_valid():
        info_profe = profe_form.cleaned_data
        filtra_profe = Clase.objects.filter(nombre_profe__icontains=info_profe['nombre_profe'])
        context ={
            "nombre_profe": filtra_profe
        }

        return render(request, "InscripcionNatacion/buscar_profesor.html", context=context)



#Edicion de profesor
def editar_profesor(request, nombre_profe):
    get_profesor = Profesor.objects.get(nombre_profe=nombre_profe)

    if request.method == 'POST':

        info_profe = request.POST
        print(info_profe)
        get_profesor.nombre_profe = info_profe['nombre_profe']
        get_profesor.apellido_profe = info_profe['apellido_profe']

        get_profesor.save()
        return redirect('INPersonas')

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

    return redirect("INPersonas")





#Comentario
def comentarios(request):
    all_comentarios = Comentario.objects.all()
    context ={
        "comentarios": all_comentarios,
        "busqueda_form_comentarios": BuscarComentarioForm
    }
    return render(request, "InscripcionNatacion/comentarios.html", context=context)



#Comentario que ya fue creado
def crear_comentario(request):
    if request.method == "POST":
        formulario = CrearComentarioForm(request.POST)

        if formulario.is_valid():
            info_comentario = formulario.cleaned_data
            save_comentario = Comentario(
                nombre_comenta=info_comentario['nombre_comenta'],
                email_comenta=info_comentario['email_comenta'],
                tipo_coemtario=info_comentario['tipo_coemtario'],
                mensaje=info_comentario['mensaje']
            )
            save_comentario.save()
            return redirect("INComentarios")

    context ={
        "form_comentario": CrearComentarioForm(),
    }
    return render(request, "InscripcionNatacion/crear_comentario.html", context)



#Creacion del comentario
def comentario_creado(request, nombre_comenta, email_comenta, tipo_coemtario, mensaje):
    save_comentario = Comentario(
        nombre_comenta=nombre_comenta,
        email_comenta=email_comenta,
        tipo_coemtario=tipo_coemtario,
        mensaje=mensaje
    )
    save_comentario.save()
    context ={
        "nombre_comenta": nombre_comenta
    }
    return render(request, "InscripcionNatacion/guardar_comentario.html", context)



#Buscar comentario a traves de la persona
def buscar_comentario(request):
    comentario_form = BuscarComentarioForm(request.GET)

    if comentario_form.is_valid():
        info_comentario = comentario_form.cleaned_data
        filtrar_comentario = Comentario.objects.filter(nombre_comenta__icontains=info_comentario['nombre_comenta'])
        context ={
            "nombre_comenta": filtrar_comentario
        }
        return render(request, "InscripcionNatacion/buscar_comentario.html", context=context)



