from django.contrib import admin
from .models import T_Eventos

class EventoAdmin(admin.ModelAdmin):
    readonly_fields = ("fecha_creacion", )


# Register your models here.
admin.site.register(T_Eventos, EventoAdmin) 
