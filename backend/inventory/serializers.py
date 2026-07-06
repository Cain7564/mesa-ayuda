from rest_framework import serializers

from .models import (
    Marca,
    SistemaOperativo,
    Ubicacion,
    EstadoEquipo,
    Equipo,
)


class MarcaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Marca
        fields = '__all__'


class SistemaOperativoSerializer(serializers.ModelSerializer):

    class Meta:
        model = SistemaOperativo
        fields = '__all__'


class UbicacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ubicacion
        fields = '__all__'


class EstadoEquipoSerializer(serializers.ModelSerializer):

    class Meta:
        model = EstadoEquipo
        fields = '__all__'


class EquipoSerializer(serializers.ModelSerializer):

    marca_nombre = serializers.CharField(
        source='marca.nombre',
        read_only=True
    )

    estado_nombre = serializers.CharField(
        source='estado.nombre',
        read_only=True
    )

    ubicacion_nombre = serializers.CharField(
        source='ubicacion.nombre',
        read_only=True
    )

    usuario_nombre = serializers.CharField(
        source='usuario_asignado.nombre',
        read_only=True
    )

    so_nombre = serializers.CharField(
        source='sistema_operativo.nombre',
        read_only=True
    )

    class Meta:
        model = Equipo

        fields = [

            'id',

            'codigo',

            'tipo',

            'marca',
            'marca_nombre',

            'modelo',

            'numero_serie',

            'procesador',

            'memoria_ram',

            'disco',

            'sistema_operativo',
            'so_nombre',

            'direccion_ip',

            'direccion_mac',

            'usuario_asignado',
            'usuario_nombre',

            'estado',
            'estado_nombre',

            'ubicacion',
            'ubicacion_nombre',

        ]

    def validate_codigo(self, value):

        if len(value.strip()) < 4:
            raise serializers.ValidationError(
                "El código debe tener al menos 4 caracteres."
            )

        return value

    def validate_modelo(self, value):

        if len(value.strip()) < 3:
            raise serializers.ValidationError(
                "El modelo debe tener al menos 3 caracteres."
            )

        return value

    def validate_numero_serie(self, value):

        if len(value.strip()) < 6:
            raise serializers.ValidationError(
                "El número de serie debe tener al menos 6 caracteres."
            )

        return value