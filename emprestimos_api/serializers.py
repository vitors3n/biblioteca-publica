from rest_framework import serializers
from .models import EmprestimoLivro

class EmprestimoLivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmprestimoLivro
        fields = ['id', 'livro', 'recebedor', 'data_emprestimo', 'data_retorno']