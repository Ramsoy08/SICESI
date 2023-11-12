from django.urls import path, include 
from . import views

urlpatterns = [
    path('participantes/create', views.create_participante, name="create_participante")
]