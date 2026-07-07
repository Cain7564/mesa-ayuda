from rest_framework.views import APIView
from rest_framework.response import Response

from users.models import Usuario, Tecnico
from tickets.models import Ticket
from inventory.models import Equipo


class ReporteGeneralView(APIView):

    def get(self, request):

        return Response({

            "usuarios": Usuario.objects.count(),

            "tecnicos": Tecnico.objects.count(),

            "tickets": Ticket.objects.count(),

            "equipos": Equipo.objects.count(),

            "tickets_abiertos": Ticket.objects.filter(
                estado="Abierto"
            ).count(),

            "tickets_proceso": Ticket.objects.filter(
                estado="En proceso"
            ).count(),

            "tickets_cerrados": Ticket.objects.filter(
                estado="Cerrado"
            ).count(),

            "equipos_activos": Equipo.objects.filter(
                estado__nombre="Activo"
            ).count(),

            "equipos_reparacion": Equipo.objects.filter(
                estado__nombre="En reparación"
            ).count(),

            "equipos_baja": Equipo.objects.filter(
                estado__nombre="Dado de baja"
            ).count(),

            "equipos_mantenimiento": Equipo.objects.filter(
                estado__nombre="En mantenimiento"
            ).count(),

        })