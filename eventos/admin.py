from django.contrib import admin
from .models import T_Eventos, T_Participantes

class EventoAdmin(admin.ModelAdmin):
    readonly_fields = ("fecha_creacion", )

class ParticipanteAdmin(admin.ModelAdmin):
    readonly_fields = ("fecha_registro", )          


# Register your models here.
admin.site.register(T_Eventos, EventoAdmin) 
admin.site.register(T_Participantes, ParticipanteAdmin)