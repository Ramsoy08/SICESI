from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.http import HttpResponse
from .forms import EventosForm
from .models import T_Eventos
from django.utils import timezone
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'main/home.html')

def signup(request):
    
    if request.method == 'GET':
        return render(request, 'register/signup.html',{
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
                return render(request, 'register/signup.html', {
                    'form': UserCreationForm,
                    "error": 'El usuario ya existe'
                })  
    return render(request, 'register/signup.html',{
        'form': UserCreationForm,
        "error": 'Las contraseñas no coinciden'
    })  
    
@login_required    
def eventos(request):
    eventos = T_Eventos.objects.filter(user=request.user, fecha_culminado__isnull=True)
    if request.method == 'GET':
        return render(request, 'main/eventos.html', {'eventos': eventos})

@login_required    
def eventos_completados (request):
    eventos = T_Eventos.objects.filter(user=request.user, fecha_culminado__isnull=False).order_by('-fecha_culminado')
    if request.method == 'GET':
        return render(request, 'main/eventos.html', {'eventos': eventos})    

@login_required 
def create_evento(request):
    if request.method == 'POST':   
        form = EventosForm(request.POST)
        if form.is_valid(): 
            new_evento = form.save(commit=False)
            new_evento.user = request.user
            new_evento.save()
            return HttpResponse("La data ha sido guardada en la base de datos")
    else: 
        form = EventosForm()
    return render (request, 'main/create_eventos.html', {'form': form})

@login_required 
def evento_detail(request, evento_id):
    if request.method == 'GET':
        evento = get_object_or_404(T_Eventos, pk=evento_id, user=request.user)
        form = EventosForm(instance=evento)
        return render(request, 'main/evento_detail.html', {'evento': evento, 'form': form})
    else:
        try:
            evento = get_object_or_404(T_Eventos, pk=evento_id, user=request.user)      
            form = EventosForm(request.POST, instance=evento)
            form.save()
            return redirect('eventos')
        except ValueError:
            return render(request, 'main/evento_detail.html', {'evento': evento, 'form': form, 'error':"Ups! Algo salió mal actualizando los datos"})

@login_required 
def evento_completado(request, evento_id):
    evento = get_object_or_404(T_Eventos, pk=evento_id, user=request.user)
    if request.method == 'POST':
            evento.fecha_culminado = timezone.now()
            evento.save()
            return redirect('eventos')
        
@login_required    
def evento_eliminado(request, evento_id):
    evento = get_object_or_404(T_Eventos, pk=evento_id, user=request.user)
    if request.method == 'POST':
            evento.delete()
            return redirect('eventos')
                
@login_required         
def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method =='GET':
        return render(request, 'register/signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'register/signin.html', {
                'form': AuthenticationForm,
                'error': 'El nombre de usuario es incorrecto'
            })    
        else:
            login(request, user) 
            return redirect('eventos')
        
