from rest_framework import generics

from .models import (
    Marca,
    SistemaOperativo,
    Ubicacion,
    EstadoEquipo,
    Equipo,
)

from .serializers import (
    MarcaSerializer,
    SistemaOperativoSerializer,
    UbicacionSerializer,
    EstadoEquipoSerializer,
    EquipoSerializer,
)


class MarcaListCreateView(generics.ListCreateAPIView):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer


class MarcaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer


class SistemaOperativoListCreateView(generics.ListCreateAPIView):
    queryset = SistemaOperativo.objects.all()
    serializer_class = SistemaOperativoSerializer


class SistemaOperativoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SistemaOperativo.objects.all()
    serializer_class = SistemaOperativoSerializer


class UbicacionListCreateView(generics.ListCreateAPIView):
    queryset = Ubicacion.objects.all()
    serializer_class = UbicacionSerializer


class UbicacionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ubicacion.objects.all()
    serializer_class = UbicacionSerializer


class EstadoEquipoListCreateView(generics.ListCreateAPIView):
    queryset = EstadoEquipo.objects.all()
    serializer_class = EstadoEquipoSerializer


class EstadoEquipoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EstadoEquipo.objects.all()
    serializer_class = EstadoEquipoSerializer


class EquipoListCreateView(generics.ListCreateAPIView):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer


class EquipoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer