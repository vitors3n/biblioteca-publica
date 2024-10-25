from django.db import models
 
class Livro(models.Model):
    titulo = models.CharField(max_length=255, verbose_name='Título')
    autor = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, verbose_name='ISBN')
    estaEmprestado = models.BooleanField(default=False, verbose_name='Está emprestado?')

    def __str__(self):
        return self.titulo

