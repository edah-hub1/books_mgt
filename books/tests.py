
# Create your tests here.
from django.test import TestCase
from django.utils.timezone import now, timedelta
from .models import Book


class BookModelTest(TestCase):
    def test_create_book(self):
        book = Book.objects.create(
            title="Test Book",
            author="John Doe",
            publication_date=now().date() - timedelta(days=1),
            isbn="1234567890123",
            summary="Test summary.",
        )
        self.assertEqual(str(book), "Test Book")


class BookAPITest(TestCase):
    def setUp(self):
        self.book_data = {
            "title": "Test API Book",
            "author": "Jane Doe",
            "publication_date": "2020-01-01",
            "isbn": "9876543210123",
            "summary": "A test book for API.",
        }

    def test_create_book_api(self):
        response = self.client.post(
            "/api/books/", self.book_data, content_type="application/json"
        )
        self.assertEqual(response.status_code, 201)
