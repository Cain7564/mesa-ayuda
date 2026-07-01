from django.db import models
from users.models import Usuario


class Marca(models.Model):

    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class SistemaOperativo(models.Model):

    nombre = models.CharField(max_length=100)

    version = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.version}"


class Ubicacion(models.Model):

    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class EstadoEquipo(models.Model):

    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Equipo(models.Model):

    TIPO_CHOICES = [
        ('PC', 'Computadora de Escritorio'),
        ('LAPTOP', 'Laptop'),
        ('MONITOR', 'Monitor'),
        ('IMPRESORA', 'Impresora'),
    ]

    codigo = models.CharField(
        max_length=20,
        unique=True
    )

    tipo = models.CharField(
        max_length=20,
        choices=TIPO_CHOICES
    )

    marca = models.ForeignKey(
        Marca,
        on_delete=models.CASCADE
    )

    modelo = models.CharField(max_length=100)

    numero_serie = models.CharField(
        max_length=100,
        unique=True
    )

    procesador = models.CharField(max_length=100)

    memoria_ram = models.CharField(max_length=50)

    disco = models.CharField(max_length=100)

    sistema_operativo = models.ForeignKey(
        SistemaOperativo,
        on_delete=models.CASCADE
    )

    direccion_ip = models.GenericIPAddressField()

    direccion_mac = models.CharField(max_length=50)

    usuario_asignado = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name="equipos"
    )

    estado = models.ForeignKey(
        EstadoEquipo,
        on_delete=models.CASCADE
    )

    ubicacion = models.ForeignKey(
        Ubicacion,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.codigo} - {self.modelo}"