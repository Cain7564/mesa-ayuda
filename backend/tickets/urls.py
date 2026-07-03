from django.urls import path

from .views import (
    CategoriaListCreateView,
    CategoriaDetailView,
    CategoriaSimpleView,
    SLAListCreateView,
    SLADetailView,
    TicketListCreateView,
    TicketDetailView,
    SeguimientoListCreateView,
    SeguimientoDetailView,
)

urlpatterns = [

    # Categorías
    path(
        'categorias/',
        CategoriaListCreateView.as_view(),
        name='categoria-list'
    ),

    path(
        'categorias/<int:pk>/',
        CategoriaDetailView.as_view(),
        name='categoria-detail'
    ),

    # SLA
    path(
        'sla/',
        SLAListCreateView.as_view(),
        name='sla-list'
    ),

    path(
        'sla/<int:pk>/',
        SLADetailView.as_view(),
        name='sla-detail'
    ),

    # Tickets
    path(
        'tickets/',
        TicketListCreateView.as_view(),
        name='ticket-list'
    ),

    path(
        'tickets/<int:pk>/',
        TicketDetailView.as_view(),
        name='ticket-detail'
    ),

    # Seguimientos
    path(
        'seguimientos/',
        SeguimientoListCreateView.as_view(),
        name='seguimiento-list'
    ),

    path(
        'seguimientos/<int:pk>/',
        SeguimientoDetailView.as_view(),
        name='seguimiento-detail'
    ),

    path(
    'categorias/simple/',
    CategoriaSimpleView.as_view(),
    name='categorias-simple'
    ),
]