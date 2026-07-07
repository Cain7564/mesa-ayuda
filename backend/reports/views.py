from rest_framework.views import APIView
from rest_framework.response import Response

from users.models import Usuario, Tecnico
from tickets.models import Ticket
from inventory.models import Equipo


class ReporteGeneralView(APIView):

    def get(self, request):

        return Response({

            # Tickets por estado
            "tickets_abiertos": Ticket.objects.filter(
                estado="Abierto"
            ).count(),

            "tickets_proceso": Ticket.objects.filter(
                estado="En proceso"
            ).count(),

            "tickets_cerrados": Ticket.objects.filter(
                estado="Cerrado"
            ).count(),

            # Tickets por prioridad
            "tickets_alta": Ticket.objects.filter(
                prioridad="Alta"
            ).count(),

            "tickets_media": Ticket.objects.filter(
                prioridad="Media"
            ).count(),

            "tickets_baja": Ticket.objects.filter(
                prioridad="Baja"
            ).count(),

            # Inventario por estado
            "equipos_activos": Equipo.objects.filter(
                estado__nombre="Activo"
            ).count(),

            "equipos_reparacion": Equipo.objects.filter(
                estado__nombre="En reparación"
            ).count(),

            "equipos_mantenimiento": Equipo.objects.filter(
                estado__nombre="En mantenimiento"
            ).count(),

            "equipos_baja": Equipo.objects.filter(
                estado__nombre="Dado de baja"
            ).count(),

            # Equipos por tipo
            "pc": Equipo.objects.filter(
                tipo="PC"
            ).count(),

            "laptop": Equipo.objects.filter(
                tipo="LAPTOP"
            ).count(),

            "monitor": Equipo.objects.filter(
                tipo="MONITOR"
            ).count(),

            "impresora": Equipo.objects.filter(
                tipo="IMPRESORA"
            ).count(),

        })