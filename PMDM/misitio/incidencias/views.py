from django.shortcuts import render
from rest_framework import viewsets

from .models import Incidencia
from .serializers import IncidenciaSerializer

# Create your views here.
class IncidenciaViewSet(viewsets.ModelViewSet):
    queryset = Incidencia.objects.all()
    serializer_class = IncidenciaSerializer
