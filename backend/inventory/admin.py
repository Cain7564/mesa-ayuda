from django.contrib import admin

from django.contrib import admin

from .models import (
    Marca,
    SistemaOperativo,
    Ubicacion,
    EstadoEquipo,
    Equipo,
)

admin.site.register(Marca)
admin.site.register(SistemaOperativo)
admin.site.register(Ubicacion)
admin.site.register(EstadoEquipo)
admin.site.register(Equipo)