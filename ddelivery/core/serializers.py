from rest_framework import serializers
from .models import Mapa


class MapaSerializer(serializers.ModelSerializer):
    mapa = serializers.CharField()

    class Meta:
        model: Mapa
        fields = ('nome', 'mapa')
