from apps.funcionarios.models import Funcionario
from rest_framework import serializers


class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = ('nome', 'departamentos', 'empresa', 'user', 'imagem')

