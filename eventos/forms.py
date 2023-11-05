from django import forms
from .models import T_Eventos


class EventosForm(forms.Form):
    #tipo CharField
    titulo = forms.CharField(
        max_length=50,
        label="Titulo Del Evento",
        required=True
    )
    
    contenido = forms.CharField(
        max_length=500,
        label="Detalles Del Evento",
        required=True
    )
    
    #tipo_fecha
    fecha_evento = forms.DateField( 

        widget=forms.DateInput(
            attrs={
                'class': 'form-control',
                'type': "date"
            }
        ),
        initial='2023-07-10'
    )
    
