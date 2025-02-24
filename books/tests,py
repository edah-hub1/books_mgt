from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Book
from datetime import date


class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a sample book for testing.
        self.book = Book.objects.create(
            title="Sample Book",
            author="John Doe",
            publication_date=date(2020, 5, 10),
            isbn="1234567890123",
            summary="This is a sample book.",
        )
        self.valid_book_data = {
            "title": "New Book",
            "author": "Jane Smith",
            "publication_date": "2019-03-15",
            "isbn": "9876543210123",
            "summary": "A test book entry.",
        }

    def test_get_books_list(self):
        # Test retrieving the list of books.
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_book_valid(self):
        # Test creating a book with valid data.
        response = self.client.post("/api/books/", self.valid_book_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_book_invalid_isbn(self):
        # Test creating a book with an invalid ISBN.
        invalid_data = self.valid_book_data.copy()
        invalid_data["isbn"] = "12345"  # Invalid ISBN
        response = self.client.post("/api/books/", invalid_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_book_future_date(self):
        # Test creating a book with a future publication date.
        invalid_data = self.valid_book_data.copy()
        invalid_data["publication_date"] = str(
            date.today().replace(year=date.today().year + 1)
        )
        response = self.client.post("/api/books/", invalid_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_single_book(self):
        # Test retrieving a single book by ID.
        response = self.client.get(f"/api/books/{self.book.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_book(self):
        # Test updating a book.
        update_data = {"title": "Updated Title", "author": "Updated Author"}
        response = self.client.patch(
            f"/api/books/{self.book.id}/", update_data, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_book(self):
        # Test deleting a book.
        response = self.client.delete(f"/api/books/{self.book.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
