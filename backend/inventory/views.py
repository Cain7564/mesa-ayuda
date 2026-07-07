from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from django.db.models import Max

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

    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
        SearchFilter,
    ]

    filterset_fields = [
        'tipo',
        'marca',
        'estado',
        'ubicacion',
        'sistema_operativo',
    ]

    search_fields = [
        'codigo',
        'modelo',
        'numero_serie',
    ]

    ordering_fields = [
        'codigo',
        'modelo',
        'tipo',
    ]

    def perform_create(self, serializer):

        tipo = serializer.validated_data["tipo"]

        prefijos = {
            "PC": "PC",
            "LAPTOP": "LP",
            "MONITOR": "MON",
            "IMPRESORA": "IMP"
        }

        prefijo = prefijos.get(tipo, "EQ")

        ultimo = Equipo.objects.filter(
            codigo__startswith=prefijo
        ).order_by("-codigo").first()

        if ultimo:

            try:

                numero = int(
                    ultimo.codigo.split("-")[1]
                ) + 1

            except Exception:

                numero = 1

        else:

            numero = 1

        codigo = f"{prefijo}-{numero:03d}"

        serializer.save(
            codigo=codigo
        )


class EquipoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer



