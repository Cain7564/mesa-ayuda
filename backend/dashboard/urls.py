from django.urls import path

from .views import (
    DashboardUsuariosView,
    DashboardTicketsView,
)

urlpatterns = [

    path(
        'dashboard/usuarios/',
        DashboardUsuariosView.as_view(),
        name='dashboard-usuarios'
    ),

    path(
        'dashboard/tickets/',
        DashboardTicketsView.as_view(),
        name='dashboard-tickets'
    ),
]