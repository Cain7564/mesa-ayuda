from rest_framework import generics, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated


from .models import Usuario
from .serializers import UsuarioSerializer
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