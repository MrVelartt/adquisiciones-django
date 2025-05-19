# views.py
import reversion
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from reversion.models import Version

from .models import Acquisition
from .serializers import AcquisitionSerializer, VersionSerializer

class AcquisitionListCreateAPIView(APIView):
    """
    GET: Lista todas las adquisiciones.
    POST: Crea una nueva adquisición con histórico de reversion.
    """
    def get(self, request):
        acquisitions = Acquisition.objects.all().order_by('-fecha_adquisicion')
        serializer = AcquisitionSerializer(acquisitions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AcquisitionSerializer(data=request.data)
        if serializer.is_valid():
            with reversion.create_revision():
                instance = serializer.save()
                reversion.set_comment("Creación de adquisición")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AcquisitionDetailAPIView(APIView):
    """
    GET: Recupera una adquisición específica.
    PUT: Reemplaza la adquisición y registra histórico completo.
    PATCH: Actualiza parcialmente y registra histórico.
    DELETE: Desactiva lógicamente la adquisición y registra histórico.
    """
    def get_object(self, pk):
        return get_object_or_404(Acquisition, pk=pk)

    def get(self, request, pk):
        acquisition = self.get_object(pk)
        serializer = AcquisitionSerializer(acquisition)
        return Response(serializer.data)

    def put(self, request, pk):
        acquisition = self.get_object(pk)
        serializer = AcquisitionSerializer(acquisition, data=request.data)
        if serializer.is_valid():
            with reversion.create_revision():
                serializer.save()
                reversion.set_comment("Actualización completa de adquisición")
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        acquisition = self.get_object(pk)
        serializer = AcquisitionSerializer(acquisition, data=request.data, partial=True)
        if serializer.is_valid():
            with reversion.create_revision():
                serializer.save()
                reversion.set_comment("Actualización parcial de adquisición")
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        acquisition = self.get_object(pk)
        with reversion.create_revision():
            acquisition.activa = False
            acquisition.save()
            reversion.set_comment("Desactivación lógica de adquisición")
        return Response({'mensaje': 'Adquisición desactivada.'}, status=status.HTTP_204_NO_CONTENT)

class AcquisitionHistorialAPIView(APIView):
    """
    GET: Lista las versiones (historial) de una adquisición.
    """
    def get(self, request, pk):
        adquisicion = get_object_or_404(Acquisition, pk=pk)
        versions = Version.objects.get_for_object(adquisicion).order_by('-revision__date_created')
        serializer = VersionSerializer(versions, many=True)
        return Response({
            'count': versions.count(),
            'results': serializer.data
        })