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

    class Meta:
        model = Equipo
        fields = '__all__'