from django import forms
from InscripcionNatacion.models import Clase, Profesor, Usuario


#CREACIONES

#Usuario
class CrearUsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
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




#BUSQUEDAS

#Buscar Usuario
class BuscarUsuarioForm(forms.Form):

    nombre_usuario = forms.CharField(min_length=3, max_length=40)


class BuscarClaseForm(forms.Form):

    dia = forms.CharField(max_length=1)


class BuscarProfesorForm(forms.Form):

    dia = forms.CharField(min_length=3, max_length=30)


