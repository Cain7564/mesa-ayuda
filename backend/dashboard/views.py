from rest_framework.views import APIView
from rest_framework.response import Response

from users.models import Usuario, Tecnico
from tickets.models import Ticket
from inventory.models import Equipo


class DashboardUsuariosView(APIView):

    def get(self, request):

        total_usuarios = Usuario.objects.count()

        total_tecnicos = Tecnico.objects.count()

        return Response({
            "usuarios": total_usuarios,
            "tecnicos": total_tecnicos,
        })
class DashboardTicketsView(APIView):

    def get(self, request):

        total = Ticket.objects.count()

        abiertos = Ticket.objects.filter(
            estado="Abierto"
        ).count()

        en_proceso = Ticket.objects.filter(
            estado="En proceso"
        ).count()

        cerrados = Ticket.objects.filter(
            estado="Cerrado"
        ).count()

        return Response({

            "tickets_total": total,

            "tickets_abiertos": abiertos,

            "tickets_en_proceso": en_proceso,

            "tickets_cerrados": cerrados,

        })
class DashboardInventoryView(APIView):

    def get(self, request):

        total = Equipo.objects.count()

        activos = Equipo.objects.filter(
            estado__nombre="Activo"
        ).count()

        reparacion = Equipo.objects.filter(
            estado__nombre="En reparación"
        ).count()

        baja = Equipo.objects.filter(
            estado__nombre="Dado de baja"
        ).count()

        mantenimiento = Equipo.objects.filter(
            estado__nombre="En mantenimiento"
        ).count()

        return Response({

            "equipos_total": total,

            "equipos_activos": activos,

            "equipos_reparacion": reparacion,

            "equipos_baja": baja,

            "equipos_mantenimiento": mantenimiento,

        })
class DashboardGeneralView(APIView):

    def get(self, request):

        return Response({

            # Usuarios
            "usuarios": Usuario.objects.count(),
            "tecnicos": Tecnico.objects.count(),

            # Tickets
            "tickets_total": Ticket.objects.count(),
            "tickets_abiertos": Ticket.objects.filter(
                estado="Abierto"
            ).count(),
            "tickets_en_proceso": Ticket.objects.filter(
                estado="En proceso"
            ).count(),
            "tickets_cerrados": Ticket.objects.filter(
                estado="Cerrado"
            ).count(),

            # Inventario
            "equipos_total": Equipo.objects.count(),
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