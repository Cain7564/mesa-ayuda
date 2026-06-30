from django.db import models
from users.models import Usuario, Tecnico


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class SLA(models.Model):
    prioridad = models.CharField(max_length=20)
    tiempo_respuesta = models.TimeField()
    tiempo_resolucion = models.TimeField()

    def __str__(self):
        return self.prioridad


class Ticket(models.Model):

    fecha = models.DateTimeField()

    asunto = models.CharField(max_length=150)

    descripcion = models.TextField()

    prioridad = models.CharField(max_length=20)

    estado = models.CharField(max_length=30)

    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE
    )

    tecnico = models.ForeignKey(
        Tecnico,
        on_delete=models.CASCADE
    )

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE
    )

    fecha_cierre = models.DateTimeField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.asunto


class Seguimiento(models.Model):

    ticket = models.ForeignKey(
        Ticket,
        on_delete=models.CASCADE
    )

    fecha = models.DateTimeField()

    comentario = models.TextField()

    estado = models.CharField(max_length=30)

    def __str__(self):
        return f"Seguimiento {self.ticket.id}"