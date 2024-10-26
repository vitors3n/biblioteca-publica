from rest_framework import viewsets
from .models import EmprestimoLivro
from .serializers import EmprestimoLivroSerializer

class EmprestimoLivroViewSet(viewsets.ModelViewSet):
    queryset = EmprestimoLivro.objects.all()
    serializer_class = EmprestimoLivroSerializer