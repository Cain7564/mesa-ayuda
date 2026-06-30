from rest_framework import serializers

from .models import (
    Categoria,
    SLA,
    Ticket,
    Seguimiento,
)


class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = '__all__'


class SLASerializer(serializers.ModelSerializer):

    class Meta:
        model = SLA
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = '__all__'


class SeguimientoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Seguimiento
        fields = '__all__'