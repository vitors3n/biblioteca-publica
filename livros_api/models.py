from django.db import models
 
class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13)
    estaEmprestado = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo

