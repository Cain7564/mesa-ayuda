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

    usuario_nombre = serializers.CharField(
        source='usuario.nombre',
        read_only=True
    )

    tecnico_nombre = serializers.CharField(
        source='tecnico.nombre',
        read_only=True
    )

    categoria_nombre = serializers.CharField(
        source='categoria.nombre',
        read_only=True
    )

    class Meta:
        model = Ticket

        fields = [
            'id',
            'fecha',
            'asunto',
            'descripcion',
            'prioridad',
            'estado',

            'usuario',
            'usuario_nombre',

            'tecnico',
            'tecnico_nombre',

            'categoria',
            'categoria_nombre',

            'fecha_cierre',
        ]

        read_only_fields = [
            'fecha',
            'fecha_cierre',
        ]
    def validate_asunto(self, value):

        if len(value.strip()) < 5:
            raise serializers.ValidationError(
                "El asunto debe tener al menos 5 caracteres."
            )

        return value

    def validate_descripcion(self, value):

        if len(value.strip()) < 10:
            raise serializers.ValidationError(
                "La descripción debe tener al menos 10 caracteres."
            )

        return value

    def validate_prioridad(self, value):

        prioridades = [
            "Alta",
            "Media",
            "Baja"
        ]

        if value not in prioridades:
            raise serializers.ValidationError(
                "La prioridad debe ser Alta, Media o Baja."
            )

        return value

    def validate_estado(self, value):

        estados = [
            "Abierto",
            "En proceso",
            "Cerrado"
        ]

        if value not in estados:
            raise serializers.ValidationError(
                "El estado debe ser Abierto, En proceso o Cerrado."
            )

        return value
class SeguimientoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Seguimiento
        fields = '__all__'