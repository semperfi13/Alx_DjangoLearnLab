from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient


client = APIClient()
client.post("/books/", {"title": "new idea"}, format="json")
