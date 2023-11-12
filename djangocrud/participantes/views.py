from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.http import HttpResponse
from .forms import ParticipantesForm
from .models import T_Participantes

# Create your views here.

def create_participante(request):
    if request.method == 'POST':   
        form = ParticipantesForm(request.POST)
        if form.is_valid(): 
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            fecha_evento = form.cleaned_data['fecha_evento']
            

            new_participante = T_Participantes.objects.create(
                nombre = nombre,
                email = email,
                fecha_evento = fecha_evento,
            )

            new_participante = form.save(commit=False)
            new_participante.user = request.user
            new_participante.save()
            
            return HttpResponse("La data ha sido guardada en la base de datos")
    form = ParticipantesForm()
    return render (request, 'create_participante.html', {'form': form})

def home(request):
    return render(request, "main/home.html")

