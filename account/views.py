from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate


from account.forms import UserRegisterForm
from account.models import Avatar


# Create your views here.


def login_account(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            infomacion = form.cleaned_data
            user = authenticate(username=infomacion['username'], password=infomacion['password'])

            if user:
                login(request, user)

                return redirect("INPersonas")

            else:
                return redirect("INComentarios")

    form = AuthenticationForm()
    context = {
        "form": form,
        "titulo": "Login",
        "enviar": "Iniciar"
    }
    return render(request, "form.html", context=context)




def register_account(request):

    if request.method =="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return  redirect("accountLogin")

    form = UserRegisterForm()
    context = {
        "form": form,
        "titulo": "Registra usuario",
        "enviar": "Registrar"
    }
    return render(request, "form.html", context=context)




def edit_usuario(request):

    user = request.user

    if request.method == "POST":
        form = UserRegisterForm(request.POST, request.FILES)

        if form.is_valid():
            informacion = form.cleaned_data

            user.username = informacion["username"]
            user.email = informacion["email"]
            user.is_staff = informacion["is_staff"]

            try:
                user.avatar.imagen = informacion["imagen"]
            except:
                avatar = Avatar(user=user, imagen=informacion["imagen"])
                avatar.save()


            form.save()
            return redirect("account")


    form = UserRegisterForm(initial={
        "username": user.name,
        "email":user.email,
        "is_staff": user.is_staff
    })

    context = {
        "form": form,
        "titulo": "Editar Usuario",
        "nviar": "Editar"
    }

    return render(request, "form.html", context=context)
