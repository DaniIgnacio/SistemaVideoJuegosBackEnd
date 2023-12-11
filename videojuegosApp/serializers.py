from rest_framework import serializers
from .models import Juego, Empresa



class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields="__all__"

class JuegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Juego
        fields="__all__"