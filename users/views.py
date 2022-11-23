from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
# Create your views here.


def login_form(request):
    form = UserLoginForm()
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Usuario o contraseña incorrectos')

    ctx = {'form': form}
    return render(request, 'users/login.html', ctx)


def register_form(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Datos almacenados correctamente')
    ctx = {'form': form}
    return render(request, 'users/register.html', ctx)
