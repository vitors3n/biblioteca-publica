from rest_framework.test import APITestCase

from django.urls import reverse

class LivroListTests(APITestCase):
    def testa_livro_list_retorno_200(self):
        url = reverse('livro-listar-criar')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)