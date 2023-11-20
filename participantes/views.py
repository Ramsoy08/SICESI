from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.http import HttpResponse
from .forms import ParticipantesForm
from eventos.models import T_Participantes
from django.utils import timezone

# Create your views here.

def lparticipantes(request):
    lparticipantes = T_Participantes.objects.filter(user=request.user)
    if request.method == 'GET':
        return render(request, 'lparticipantes.html', {'lparticipantes': lparticipantes})


def create_participante(request):
    if request.method == 'POST':   
        form = ParticipantesForm(request.POST)
        if form.is_valid(): 
            new_participante = form.save(commit=False)
            new_participante.user = request.user
            new_participante.save()
            return HttpResponse("El participante ha sido guardado en la base de datos")
    else: 
        form = ParticipantesForm()
    return render (request, 'form.html', {'form': form})

def home(request):
    return render(request, "main/home.html")


def form_detail(request, participante_id):
    if request.method == 'GET':
        participante = get_object_or_404(T_Participantes, pk=participante_id, user=request.user)
        form = ParticipantesForm(instance=participante)
        return render(request, 'form_detail.html', {'participante': participante, 'form': form})
    else:
        try:
            participante = get_object_or_404(T_Participantes, pk=participante_id, user=request.user)      
            form = ParticipantesForm(request.POST, instance=participante)
            form.save()
            return redirect('lparticipantes')
        except ValueError:
            return render(request, 'form_detail.html', {'participante': participante, 'form': form, 'error':"Ups! Algo salió mal actualizando los datos"})
  
        
def participante_eliminado(request, participante_id):
    participante = get_object_or_404(T_Participantes, pk=participante_id, user=request.user)
    if request.method == 'POST':
            participante.delete()
            return redirect('lparticipantes')
                