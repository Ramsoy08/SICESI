from django.shortcuts import render
from eventos.models import T_Eventos
from eventos.models import T_Participantes



# Create your views here.

def participantes_por_evento(request):
    eventos = T_Eventos.objects.all()
    datos = []
    
    for evento in eventos:
        participantes = T_Participantes.objects.filter(evento=evento)
        cantidad_participantes = participantes.count()
        datos.append({
            'evento': evento.titulo,
            'participantes': cantidad_participantes
        })
    
    return render(request, 'grafica.html', {'datos': datos})
