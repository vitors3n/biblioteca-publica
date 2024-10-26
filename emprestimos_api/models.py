from django.db import models
from livros_api.models import Livro

class EmprestimoLivro(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, related_name='emprestimos')
    recebedor = models.CharField(max_length=100, verbose_name='Nome do recebedor')
    data_emprestimo = models.DateField(verbose_name='Data do emprestimo')
    data_retorno = models.DateField(null=True, blank=True, verbose_name='Data da devolução')

    class Meta:
        verbose_name = 'Emprestimo de Livro'
        verbose_name_plural = 'Emprestimos de Livros'

    def __str__(self):
        return f"{self.livro.titulo} emprestado para {self.recebedor}"
