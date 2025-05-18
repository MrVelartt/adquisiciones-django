from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Acquisition
from .serializers import AcquisitionSerializer
from django.shortcuts import get_object_or_404

class AcquisitionListCreateAPIView(APIView):
    def get(self, request):
        acquisitions = Acquisition.objects.all()
        serializer = AcquisitionSerializer(acquisitions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AcquisitionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AcquisitionDetailAPIView(APIView):
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
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        acquisition = self.get_object(pk)
        serializer = AcquisitionSerializer(acquisition, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        acquisition = self.get_object(pk)
        acquisition.activo = False  # desactivación lógica
        acquisition.save()
        return Response({'mensaje': 'Adquisición desactivada.'}, status=status.HTTP_204_NO_CONTENT)
