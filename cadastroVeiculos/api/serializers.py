from rest_framework import serializers
from .models import Veiculos


class VeiculosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Veiculos
        fields = ['veiculo', 'marca', 'ano', 'descricao', 'vendido']
