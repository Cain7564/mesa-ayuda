from django.contrib import admin
from .models import Categoria, SLA, Ticket, Seguimiento

admin.site.register(Categoria)
admin.site.register(SLA)
admin.site.register(Ticket)
admin.site.register(Seguimiento)