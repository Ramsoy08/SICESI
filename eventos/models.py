from django.db import models 
from django.contrib.auth.models import User

# Create your models here.
    
# class orquestas(models.Model):
#     nombre = models.CharField(max_length=200)
#     estado = models.CharField(max_length=100)
#     nombre_completo_coordinador = models.TextField(blank=True)
#     telefono = models.IntegerField
#     correo = models.EmailField


class T_Eventos(models.Model):
    titulo = models.CharField (max_length=100)
    contenido = models.TextField(blank=True)
    fecha_evento = models.DateTimeField(default=None, blank=True) 
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_culminado = models.DateTimeField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
#    orquesta = models.ForeignKey(orquestas, related_name="orquestas",  on_delete=models.CASCADE )
    
    def __str__ (self):
        return self.titulo

class T_Participantes(models.Model):
    nacionalidad_choices = [
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
    
    
    pais_residencia = [
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
    
    
    nombres = models.CharField (max_length=50, null=False, blank=False)
    apellidos = models.CharField (max_length=50, null=False, blank=False)
    nacionalidad = models.CharField (choices=nacionalidad_choices, null=True, blank=True, max_length=50)
    pais_residencia = models.CharField (choices=pais_residencia, null=True, blank=True, max_length=50)
    ciudad_residencia = models.CharField (max_length=100, null=False, blank=False)
    correo = models.EmailField (null=False, blank=False)
    tipo_documento = models.CharField (choices=documento_choice, null=True, blank=True, max_length=50)
    n_documento = models.IntegerField (null=False, blank=False)
    telefono = models.IntegerField (null=False, blank=False)
    profesion = models.CharField (max_length=100)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    evento = models.ForeignKey (T_Eventos, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    
    def __str__ (self):
        return self.nombres

