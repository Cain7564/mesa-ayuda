from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

from .models import Usuario
from .serializers import UsuarioSerializer


class UsuarioListCreateView(generics.ListCreateAPIView):

    queryset = Usuario.objects.all()

    serializer_class = UsuarioSerializer

    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
    ]

    filterset_fields = [
        'rol',
    ]

    ordering_fields = [
        'nombre',
        'correo',
        'rol',
    ]

class UsuarioDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Usuario.objects.all()

    serializer_class = UsuarioSerializer