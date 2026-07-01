from rest_framework.views import APIView
from rest_framework.response import Response

from users.models import Usuario, Tecnico


class DashboardUsuariosView(APIView):

    def get(self, request):

        total_usuarios = Usuario.objects.count()

        total_tecnicos = Tecnico.objects.count()

        return Response({
            "usuarios": total_usuarios,
            "tecnicos": total_tecnicos,
        })