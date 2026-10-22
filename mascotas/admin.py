from django.contrib import admin
from .models import Mascota, Cita


@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "especie", "raza", "nombre_dueno")
    search_fields = ("nombre", "nombre_dueno")


@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ("mascota", "fecha", "hora", "estado", "motivo")
    list_filter = ("fecha", "estado")
    search_fields = ("mascota__nombre", "mascota__nombre_dueno")
