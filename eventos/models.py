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
    fecha_evento = models.DateTimeField(default=None) 
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
#    orquesta = models.ForeignKey(orquestas, related_name="orquestas",  on_delete=models.CASCADE )
    
    def __str__ (self):
        return self.titulo