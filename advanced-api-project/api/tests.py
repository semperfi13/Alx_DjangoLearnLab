from django.test import TestCase
from api.models import Book


# Create your tests here.
class BokkTestCase(TestCase):
    def setUp(self):
        Book.objects.create(title="LION", publication_year=1980)
        Book.objects.create(title="CAT", publication_year=2024)

    def test_book(self):
        book = Book.objects.get(title="LION")
        self.assertEqual(book.title, "LION")
