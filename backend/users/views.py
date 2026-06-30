from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from .models import Usuario
from .serializers import UsuarioSerializer


class UsuarioListCreateView(generics.ListCreateAPIView):

    queryset = Usuario.objects.all()

    serializer_class = UsuarioSerializer

    filter_backends = [DjangoFilterBackend]

    filterset_fields = ['rol']


class UsuarioDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Usuario.objects.all()

    serializer_class = UsuarioSerializer