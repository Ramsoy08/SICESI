from django import forms
from .models import T_Eventos


class EventosForm(forms.ModelForm):
    #tipo CharField
    titulo = forms.CharField(
        max_length=500,
        label="Titulo Del Evento",
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': "text"
            }
        ),
    )
    
    contenido = forms.CharField(
        max_length=500,
        label="Detalles Del Evento",
        required=True,
                widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'type': "text"
            }
        ),
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
    
    class Meta:
        model = T_Eventos
        fields = ['titulo','contenido','fecha_evento']
