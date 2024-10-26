from django.urls import path
from .views import LivroListCreateAPIView, LivroDetailAPIView

urlpatterns = [
    path('livros/', LivroListCreateAPIView.as_view(), name='livro-listar-criar'),
    path('livros/<int:pk>/', LivroDetailAPIView.as_view(), name='livro-editar-deletar'),
]