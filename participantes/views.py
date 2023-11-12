from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.http import HttpResponse
from .forms import ParticipantesForm
from eventos.models import T_Participantes

# Create your views here.

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


