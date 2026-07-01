from django.urls import path

from .views import DashboardUsuariosView

urlpatterns = [

    path(
        'dashboard/usuarios/',
        DashboardUsuariosView.as_view(),
        name='dashboard-usuarios'
    ),
]