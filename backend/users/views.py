from rest_framework import generics, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


from .models import Usuario, Tecnico
from .serializers import UsuarioSerializer, TecnicoSerializer
from .permissions import EsAdministrador


class UsuarioListCreateView(generics.ListCreateAPIView):

    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [
        DjangoFilterBackend,
        OrderingFilter,
        SearchFilter
    ]

    filterset_fields = ['rol']

    search_fields = [
        'nombre',
        'correo',
    ]

    ordering_fields = [
        'nombre',
        'correo',
        'rol',
    ]

    def get_queryset(self):
        print("Usuario autenticado:", self.request.user)
        return Usuario.objects.all().order_by('id')

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        print("===== ERRORES DEL SERIALIZER =====")
        print(serializer.errors)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class UsuarioDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [IsAuthenticated]

class UsuarioSimpleView(APIView):

    def get(self, request):

        usuarios = Usuario.objects.values(
            "id",
            "nombre"
        )

        return Response(list(usuarios))
    
class TecnicoSimpleView(APIView):

    def get(self, request):

        tecnicos = Tecnico.objects.values(
            "id",
            "nombre"
        )

        return Response(list(tecnicos))
    
class TecnicoListCreateView(generics.ListCreateAPIView):

    queryset = Tecnico.objects.all()

    serializer_class = TecnicoSerializer

    permission_classes = [IsAuthenticated]

    filter_backends = [
        SearchFilter,
        OrderingFilter,
    ]

    search_fields = [
        'nombre',
        'especialidad',
    ]

    ordering_fields = [
        'nombre',
        'especialidad',
    ]


class TecnicoDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Tecnico.objects.all()

    serializer_class = TecnicoSerializer

    permission_classes = [IsAuthenticated]

class TecnicoListCreateView(generics.ListCreateAPIView):

    queryset = Tecnico.objects.all()

    serializer_class = TecnicoSerializer

    permission_classes = [IsAuthenticated]

    filter_backends = [
        SearchFilter,
        OrderingFilter,
    ]

    search_fields = [
        'nombre',
        'especialidad',
    ]

    ordering_fields = [
        'nombre',
        'especialidad',
    ]


class TecnicoDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Tecnico.objects.all()

    serializer_class = TecnicoSerializer

    permission_classes = [IsAuthenticated]