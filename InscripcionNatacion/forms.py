from django import forms
from InscripcionNatacion.models import Clase, Profesor, Usuario



#Usuario
#Creacion del usuario en el formulario
class CrearUsuarioForm(forms.ModelForm):

    nombre = forms.CharField(min_length=3, max_length=40)
    nombre_usuario = forms.CharField(min_length=3, max_length=40)
    contrasenia = forms.CharField(min_length=3, max_length=40)
    mail = forms.CharField(min_length=3, max_length=40)




#Clases
class CrearClaseForm(forms.ModelForm):
    class Meta:
        model = Clase
        fields = "__all__"



class EditarClaseForm(forms.ModelForm):
    class Meta:
        model = Clase
        fields = "__all__"



#Buscar Usuario
class BuscarUsuarioForm(forms.Form):

    nombre_usuario = forms.CharField(min_length=3, max_length=40)


