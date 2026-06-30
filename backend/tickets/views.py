from django.shortcuts import render
from rest_framework import generics

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


class TicketDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class SeguimientoListCreateView(generics.ListCreateAPIView):
    queryset = Seguimiento.objects.all()
    serializer_class = SeguimientoSerializer


class SeguimientoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Seguimiento.objects.all()
    serializer_class = SeguimientoSerializer
