from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.http import HttpResponse
from .forms import EventosForm
from .models import T_Eventos


def home(request):
    return render(request, 'home.html')

def signup(request):
    
    if request.method == 'GET':
        return render(request, 'signup.html',{
            'form': UserCreationForm
        })   
    else:
        if request.POST['password1'] == request.POST['password2']:
            # register user
            try:
                user = User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect(eventos)
            except:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    "error": 'El usuario ya existe'
                })  
    return render(request, 'signup.html',{
        'form': UserCreationForm,
        "error": 'Las contraseñas no coinciden'
    })  
    
def eventos(request):
    if request.method == 'GET':
        return render(request, 'eventos.html')

def create_evento(request):
    if request.method == 'POST':   
        form = EventosForm(request.POST)
        if form.is_valid(): 
            titulo = form.cleaned_data['titulo']
            contenido = form.cleaned_data['contenido']
            fecha_evento = form.cleaned_data['fecha_evento']
            

            new_evento = T_Eventos.objects.create(
                titulo = titulo,
                contenido = contenido,
                fecha_evento = fecha_evento,
            )

            new_evento = form.save(commit=False)
            new_evento.user = request.user
            new_evento.save()
            
            return HttpResponse("La data ha sido guardada en la base de datos")
    form = EventosForm()
    return render (request, 'create_eventos.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method =='GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'El nombre de usuario es incorrecto'
            })    
        else:
            login(request, user) 
            return redirect('eventos')
        
