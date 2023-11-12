from django.contrib import admin
from .models import T_Participantes

class ParticipanteAdmin(admin.ModelAdmin):
    readonly_fields = ("fecha_creacion", )


# Register your models here.
admin.site.register(T_Participantes, ParticipanteAdmin) 
# Register your models here.
