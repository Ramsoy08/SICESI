from django import forms
from eventos.models import T_Participantes, T_Eventos

class ParticipantesForm(forms.ModelForm):
    
    nacionalidad_choice = [
        ("Afgano / Afgana", "Afgano / Afgana"),
        ("Alemán / Alemana", "	Alemán /Alemana"),
        ("Arabe", "Arabe"),
        ("Argentino/Argentina", "Argentino/Argentina"),
        ("Australiano/Australiana", "Australiano/Australiana"),
        ("Belga", "Belga"),
        ("Boliviano/Boliviana", "Boliviano/Boliviana"),
        ("Brasileño/Brasileña", "Brasileño/Brasileña"),
        ("Camboyano/Camboyana", "Camboyano/Camboyana"),
        ("Canadiense", "Canadiense"),
        ("Chileno/Chilena", "Chileno/Chilena"),
        ("Chino/China", "Chino/China"),
        ("Colombiano/Colombiana", "Colombiano/Colombiana"),
        ("Coreano/Coreana", "Coreano/Coreana"),
        ("Costarricense", "Costarricense"),
        ("Cubano/Cubana", "Cubano/Cubana"),
        ("Danés/Danesa", "Danés/Danesa"),
        ("Ecuatoriano/Ecuatoriana", "Ecuatoriano/Ecuatoriana"),
        ("Egipcio/Egipcia", "Egipcio/Egipcia"),
        ("Salvadoreño/Salvadoreña", "Salvadoreño/Salvadoreña"),
        ("Escocés/Escocesa", "Escocés/Escocesa"),
        ("Español/Española", "Español/Española"),
        ("Estadounidense", "Estadounidense"),
        ("Escocés/Escocesa", "Escocés/Escocesa"),
        ("Estonio/Estonia", "Estonio/Estonia"),
        ("Etiope", "Etiope"),
        ("Filipino/Filipina", "Filipino/Filipina"),
        ("Finlandés/Finlandesa", "Finlandés/Finlandesa"),
        ("Francés/Francesa", "Francés/Francesa"),
        ("Gales/Galesa", "Gales/Galesa"),
        ("Griego/Griega", "Griego/Griega"),
        ("Guatemalteco/Guatemalteca", "Guatemalteco/Guatemalteca"),
        ("Haitiano/Haitiana", "Haitiano/Haitiana"),
        ("Holandés/Holandesa", "Holandés/Holandesa"),
        ("Hondureño/Hondureña", "Hondureño/Hondureña"),
        ("Escocés/Escocesa", "Escocés/Escocesa"),
        ("Indonés/Indonesa", "Indonés/Indonesa"),
        ("Inglés/Inglesa", "Inglés/Inglesa"),
        ("Iraquí", "Iraquí"),
        ("Iraní", "Iraní"),
        ("Irlandés/Irlandesa", "Irlandés/Irlandesa"),
        ("Israelí", "Israelí"),
        ("Italiano/Italiana", "Italiano/Italiana"),
        ("Japonés/Japonesa", "Japonés/Japonesa"),
        ("Jordano/Jordana", "Jordano/Jordana"),
        ("Laosiano/Laosiana", "Laosiano/Laosiana"),
        ("Letón/Letona", "Letón/Letona"),
        ("Letonés/Letonesa", "Letonés/Letonesa"),
        ("Malayo/Malaya", "Malayo/Malaya"),
        ("Marroquí", "Marroquí"),
        ("Mexicano/Mexicana","Mexicano/Mexicana"),
        ("Nicaragüense", "Nicaragüense"),
        ("Noruego/Noruega", "Noruego/Noruega"),
        ("Neozelandés/Neozelandesa", "Neozelandés/Neozelandesa"),
        ("Panameño/Panameña", "Panameño/Panameña"),
        ("Paraguayo/Paraguaya", "Paraguayo/Paraguaya"),
        ("Peruano/Peruana", "Peruano/Peruana"),
        ("Polaco/Polaca", "Polaco/Polaca"),
        ("Portugués/Portuguesa", "Portugués/Portuguesa"),
        ("Puertorriqueño", "Puertorriqueño"),
        ("Dominicano/Dominicana", "Dominicano/Dominicana"),
        ("Rumano/Rumana", "Rumano/Rumana"),
        ("Ruso/Rusa", "Ruso/Rusa"),
        ("Sueco/Sueca", "Sueco/Sueca"),
        ("Suizo/Suiza", "Suizo/Suiza"),
        ("Tailandés/Tailandesa", "Tailandés/Tailandesa"),
        ("Taiwanes/Taiwanesa", "Taiwanes/Taiwanesa"),
        ("Turco/Turca", "Turco/Turca"),
        ("Ucraniano/Ucraniana", "Ucraniano/Ucraniana"),
        ("Uruguayo/Uruguaya", "Uruguayo/Uruguaya"),
        ("Venezolano/Venezolana", "Venezolano/Venezolana"),
        ("Vietnamita", "Vietnamita")
    ]
    
    
    pais_residencia_choice = [
        ("Afganistán", "Afganistán"),
        ("Alemania", "Alemania"),
        ("Arabia Saudita", "Arabia Saudita"),
        ("Argentina", "Argentina"),
        ("Australia", "Australia"),
        ("Bélgica", "Bélgica"),
        ("Bolivia", "Bolivia"),
        ("Brasil", "Brasil"),
        ("Camboya", "Camboya"),
        ("Canadá", "Canadá"),
        ("Chile", "Chile"),
        ("China", "China"),
        ("Colombia", "Colombia"),
        ("Corea del Sur", "Corea del Sur"),
        ("Costa Rica", "Costa Rica"),
        ("Cuba", "Cuba"),
        ("Dinamarca", "Dinamarca"),
        ("Ecuador", "Ecuador"),
        ("Egipto", "Egipto"),
        ("El Salvador", "El Salvador"),
        ("Escocia", "Escocia"),
        ("España", "España"),
        ("Estados Unidos", "Estados Unidos"),
        ("Estonia", "Estonia"),
        ("Etiopia", "Etiopia"),
        ("Filipinas", "Filipinas"),
        ("Finlandia", "Finlandia"),
        ("Francia", "Francia"),
        ("Gales", "Gales"),
        ("Grecia", "Grecia"),
        ("Guatemala", "Guatemala"),
        ("Haití", "Haití"),
        ("Holanda", "Holanda"),
        ("Honduras", "Honduras"),
        ("Gales", "Gales"),
        ("Indonesia", "Indonesia"),
        ("Inglaterra", "Inglaterra"),
        ("Irak", "Irak"),
        ("Irán", "Irán"),
        ("Irlanda", "Irlanda"),
        ("Israel", "Israel"),
        ("Italia", "Italia"),
        ("Japón", "Japón"),
        ("Jordania", "Jordania"),
        ("Laos", "Laos"),
        ("Letonia", "Letonia"),
        ("Lituania", "Lituania"),
        ("Malasia", "Malasia"),
        ("Marruecos", "Marruecos"),
        ("México", "México"),
        ("Nicaragua", "Nicaragua"),
        ("Noruega", "Noruega"),
        ("Nueva Zelandia", "Nueva Zelandia"),
        ("Panamá", "Panamá"),
        ("Paraguay", "Paraguay"),
        ("Perú", "Perú"),
        ("Polonia", "Polonia"),
        ("Portugal", "Portugal"),
        ("Puerto Rico", "Puerto Rico"),
        ("Republica Dominicana", "Republica Dominicana"),
        ("Rumania", "Rumania"),
        ("Rusia", "Rusia"),
        ("Suecia", "Suecia"),
        ("Suiza", "Suiza"),
        ("Tailandia", "Tailandia"),
        ("Taiwán", "Taiwán"),
        ("Turquía", "Turquía"),
        ("Ucrania", "Ucrania"),
        ("Uruguay", "Uruguay"),
        ("Venezuela", "Venezuela"),
        ("Vietnam", "Vietnam")
    ]
    
    documento_choice = [
        ("Cedula de Identidad", "Cedula de Identidad"),
        ("Pasaporte", "Pasaporte"),
        ("RIF", "RIF")
    ]
     
    #tipo CharField
    nombres = forms.CharField(
        max_length=50,
        label="Nombres del participante",
        required=True,
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'type' : "text",
            }
        ),
    )
    
    apellidos = forms.CharField(
        max_length=50,
        label="Apellidos del participante",
        required=True,
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'type' : "text",
            }
        ),
    )
    
    correo = forms.EmailField(
        label="Email del participante",
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class' : 'form-control',
                'type' : "text",
                'placeholder' : "ejemplo@email.com",
            }
        ),
    )
    
    ciudad_residencia = forms.CharField(
        max_length=50,
        label="Ciudad en la que reside",
        required=True,
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'type' : "text",
            }
        ),
    )
    
    profesion = forms.CharField(
        max_length=50,
        label="Profesion",
        required=True,
        widget=forms.TextInput(
            attrs={
                'class' : 'form-control',
                'type' : "text",
            }
        ),
    )
    
    #tipo_integerfield
    n_documento = forms.IntegerField(
        label="Número de Documento",
        required=True,
        widget=forms.NumberInput(
            attrs={
                'class' : 'form-control',
                'type' : "number",
                'id' : "documento",
            }
        ),
    )
    
    telefono = forms.IntegerField(
        label="Número de Telefono",
        required=True,
        widget=forms.NumberInput(
            attrs={
                'class' : 'form-control',
                'type' : "number",
                'id' : "telefono",
            }
        ),
    )
    
    #tipo choicefield
    nacionalidad = forms.ChoiceField(
        choices=nacionalidad_choice,
        label="Nacionalidad",
        required=True,
        widget=forms.Select(
            attrs={
                'class' : 'form-control',
            }
        ),
    )
    
    pais_residencia = forms.ChoiceField(
        choices=pais_residencia_choice,
        label="Pais",
        required=True,
        widget=forms.Select(
            attrs={
                'class' : 'form-control',
            }
        ),
    )
    
    tipo_documento = forms.ChoiceField(
        choices=documento_choice,
        label="Tipo de documento",
        required=True,
        widget=forms.Select(
            attrs={
                'class' : 'form-control',
            }
        ),
    )
    


    class Meta:
        model = T_Participantes
        fields = ['nombres','apellidos','nacionalidad','pais_residencia','ciudad_residencia','correo','tipo_documento',
                  'n_documento','telefono','profesion','evento']