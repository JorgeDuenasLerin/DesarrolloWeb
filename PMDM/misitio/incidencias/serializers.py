from rest_framework import serializers

from .models import Incidencia

class IncidenciaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Incidencia
        fields = ['estado', 'lugar', 'descripcion']
