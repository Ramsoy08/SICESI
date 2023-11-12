from django import forms
from .models import T_Participantes



class ParticipantesForm(forms.Form):
    #tipo CharField
    nombre = forms.CharField(
        max_length=50,
        label="Nombre del participante",
        required=True
        
    )
    
    email = forms.EmailField(
        label="Email del participante",
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
    

    
    def clean_registro_nombre(self):
        nombre = self.cleaned_data['nombre']
        if nombre == "":
            raise forms.ValidationError("The name field cannot be empty")

        if nombre == "Nombre":
            raise forms.ValidationError("Please enter a valid name")
        return nombre

    nombre = forms.CharField(
        max_length=50,
        label="Employee Name",
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        }),
        initial="Name",
    )