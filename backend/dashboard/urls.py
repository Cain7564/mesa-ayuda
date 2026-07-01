from django.urls import path

from .views import (
    DashboardUsuariosView,
    DashboardTicketsView,
    DashboardInventoryView,
    DashboardGeneralView,
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

    path(
        'dashboard/inventory/',
        DashboardInventoryView.as_view(),
        name='dashboard-inventory'
    ),

    path(
        'dashboard/general/',
        DashboardGeneralView.as_view(),
        name='dashboard-general'
    ),
]