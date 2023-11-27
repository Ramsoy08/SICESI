from django.urls import path
from . import views

urlpatterns = [
    path('grafica_eventos/', views.participantes_por_evento, name='grafica_eventos')
]