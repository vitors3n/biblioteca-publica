from django.urls import path
from .views import LivroListCreateAPIView, LivroDetailAPIView

urlpatterns = [
    path('livros/', LivroListCreateAPIView.as_view(), name='book-list-create'),
    path('livros/<int:pk>/', LivroDetailAPIView.as_view(), name='book-detail'),
]