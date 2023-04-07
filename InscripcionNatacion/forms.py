from django import forms
from InscripcionNatacion.models import Clase, Profesor, DatosPersona, Comentario


#CREACIONES

#Personas
class CrearPersonaForm(forms.ModelForm):

    class Meta:
        model = DatosPersona
        fields = "__all__"


#Clases
class CrearClaseForm(forms.ModelForm):
    class Meta:
        model = Clase
        fields = "__all__"


#Profesor
class CrearProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = "__all__"


class CrearComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = "__all__"



#BUSQUEDAS

#Buscar Usuario
class BuscarPersonaForm(forms.Form):

    apellido = forms.CharField(min_length=3, max_length=40)


class BuscarClaseForm(forms.Form):

    dia = forms.CharField(max_length=1)


class BuscarProfesorForm(forms.Form):

    nombre_profe = forms.CharField(min_length=3, max_length=30)


class BuscarComentarioForm(forms.Form):

    nombre_comenta = forms.CharField(min_length=3, max_length=30)

