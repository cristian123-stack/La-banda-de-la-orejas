from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import *

def home(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # o a donde quieras redirigir tras login
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos')

    return render(request, 'home.html')

def sobrenosotros(request):  
    return render(request, 'sobrenosotros.html')  

def contacto(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el mensaje en la base de datos
            messages.success(request, 'Tu mensaje ha sido enviado con éxito.')
            return redirect('contacto')  # Redirige a la misma página o a donde quieras
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = ContactForm()

    return render(request, 'contacto.html', {'form': form})

