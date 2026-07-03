from django.urls import path

from .views import (
    UsuarioListCreateView,
    UsuarioDetailView,
    UsuarioSimpleView,
    TecnicoSimpleView,
    TecnicoListCreateView,
    TecnicoDetailView,
)

urlpatterns = [

    path(
        '',
        UsuarioListCreateView.as_view(),
        name='usuarios'
    ),

    path(
        '<int:pk>/',
        UsuarioDetailView.as_view(),
        name='usuario-detail'
    ),

    path(
        'simple/',
        UsuarioSimpleView.as_view(),
        name='usuarios-simple'
    ),

    path(
        'tecnicos/simple/',
        TecnicoSimpleView.as_view(),
        name='tecnicos-simple'
    ),

    # CRUD de Técnicos
    path(
        'tecnicos/',
        TecnicoListCreateView.as_view(),
        name='tecnicos'
    ),

    path(
        'tecnicos/<int:pk>/',
        TecnicoDetailView.as_view(),
        name='tecnico-detail'
    ),

]