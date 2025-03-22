from rest_framework.test import APIClient
from rest_framework.test import APITestCase, URLPatternsTestCase
from api.models import Book
from rest_framework import status
from django.urls import include, path, reverse

client = APIClient()
client.post("/books/", {"title": "new idea"}, format="json")


class BokkTestCase(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path("api/", include("api.urls")),
    ]

    def setUp(self):
        Book.objects.create(title="LION", publication_year=1980)
        Book.objects.create(title="CAT", publication_year=2024)

    def test_book(self):
        url = reverse("books")
        response = self.client.get(url, format="json")
        self.client.login(username="lauren", password="secret")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
