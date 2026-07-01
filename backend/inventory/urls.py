from django.urls import path

from .views import (
    MarcaListCreateView,
    MarcaDetailView,
    SistemaOperativoListCreateView,
    SistemaOperativoDetailView,
    UbicacionListCreateView,
    UbicacionDetailView,
    EstadoEquipoListCreateView,
    EstadoEquipoDetailView,
    EquipoListCreateView,
    EquipoDetailView,
)

urlpatterns = [

    # Marca
    path(
        'marcas/',
        MarcaListCreateView.as_view(),
        name='marca-list'
    ),

    path(
        'marcas/<int:pk>/',
        MarcaDetailView.as_view(),
        name='marca-detail'
    ),

    # Sistema Operativo
    path(
        'sistemas-operativos/',
        SistemaOperativoListCreateView.as_view(),
        name='so-list'
    ),

    path(
        'sistemas-operativos/<int:pk>/',
        SistemaOperativoDetailView.as_view(),
        name='so-detail'
    ),

    # Ubicación
    path(
        'ubicaciones/',
        UbicacionListCreateView.as_view(),
        name='ubicacion-list'
    ),

    path(
        'ubicaciones/<int:pk>/',
        UbicacionDetailView.as_view(),
        name='ubicacion-detail'
    ),

    # Estado Equipo
    path(
        'estados-equipo/',
        EstadoEquipoListCreateView.as_view(),
        name='estado-list'
    ),

    path(
        'estados-equipo/<int:pk>/',
        EstadoEquipoDetailView.as_view(),
        name='estado-detail'
    ),

    # Equipos
    path(
        'equipos/',
        EquipoListCreateView.as_view(),
        name='equipo-list'
    ),

    path(
        'equipos/<int:pk>/',
        EquipoDetailView.as_view(),
        name='equipo-detail'
    ),
]