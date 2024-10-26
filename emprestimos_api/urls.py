from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmprestimoLivroViewSet

router = DefaultRouter()
router.register(r'emprestimos', EmprestimoLivroViewSet)

urlpatterns = [
    path('', include(router.urls)),
]