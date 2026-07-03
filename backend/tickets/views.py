from django.utils import timezone

from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.views import APIView
from rest_framework.response import Response



from .models import (
    Categoria,
    SLA,
    Ticket,
    Seguimiento,
)

from .serializers import (
    CategoriaSerializer,
    SLASerializer,
    TicketSerializer,
    SeguimientoSerializer,
)


class CategoriaListCreateView(generics.ListCreateAPIView):

    queryset = Categoria.objects.all()

    serializer_class = CategoriaSerializer


class CategoriaDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Categoria.objects.all()

    serializer_class = CategoriaSerializer


class SLAListCreateView(generics.ListCreateAPIView):

    queryset = SLA.objects.all()

    serializer_class = SLASerializer


class SLADetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = SLA.objects.all()

    serializer_class = SLASerializer


class TicketListCreateView(generics.ListCreateAPIView):

    queryset = Ticket.objects.all()

    serializer_class = TicketSerializer

    filter_backends = [

        DjangoFilterBackend,

        OrderingFilter,

        SearchFilter,

    ]

    filterset_fields = [

        'estado',

        'prioridad',

        'categoria',

        'tecnico',

    ]

    search_fields = [

        'asunto',

        'descripcion',

    ]

    ordering_fields = [

        'fecha',

        'prioridad',

        'estado',

    ]

    def perform_create(self, serializer):

        serializer.save(

            fecha=timezone.now()

        )


class TicketDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Ticket.objects.all()

    serializer_class = TicketSerializer


class SeguimientoListCreateView(generics.ListCreateAPIView):

    queryset = Seguimiento.objects.all()

    serializer_class = SeguimientoSerializer


class SeguimientoDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Seguimiento.objects.all()

    serializer_class = SeguimientoSerializer

class CategoriaSimpleView(APIView):

    def get(self, request):

        categorias = Categoria.objects.all().values(

            'id',

            'nombre'

        )
