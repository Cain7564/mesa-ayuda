from rest_framework.views import APIView
from rest_framework.response import Response

from users.models import Usuario, Tecnico
from tickets.models import Ticket


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