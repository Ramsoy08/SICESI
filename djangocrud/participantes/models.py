from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class T_Participantes(models.Model):
    nombre = models.CharField (max_length=100)
    contenido = models.TextField(blank=True)
    fecha_evento = models.DateTimeField(default=None) 
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    
    def __str__ (self):
        return self.titulo