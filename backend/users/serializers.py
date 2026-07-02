from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from .models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario
        fields = '__all__'
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def validate_nombre(self, value):

        if len(value.strip()) < 3:
            raise serializers.ValidationError(
                "El nombre debe tener al menos 3 caracteres."
            )

        return value

    def validate_password(self, value):

        if len(value) < 8:
            raise serializers.ValidationError(
                "La contraseña debe tener al menos 8 caracteres."
            )

        return value

    def create(self, validated_data):

        validated_data['password'] = make_password(
            validated_data['password']
        )

        return super().create(validated_data)

    def update(self, instance, validated_data):

        if 'password' in validated_data:

            validated_data['password'] = make_password(
                validated_data['password']
            )

        return super().update(instance, validated_data)