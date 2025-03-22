from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient
from django.test import TestCase
from api.models import Book

client = APIClient()
client.post("/books/", {"title": "new idea"}, format="json")


class BokkTestCase:
    def setUp(self):
        Book.objects.create(title="LION", publication_year=1980)
        Book.objects.create(title="CAT", publication_year=2024)
