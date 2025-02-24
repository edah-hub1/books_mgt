# Books Management API

## Features
- Manage books using a REST API.
- Validate ISBN and publication dates.
- CRUD operations for books.

## Setup Instructions
1. Clone the repository:
    git clone https://github.com/edah-hub1/books_mgt.git
    
2. Install dependencies:
    pip install -r requirements.txt

3. Apply Migrations
    python manage.py runserver

4. Runserver
    python manage.py runserver
    
5. Use Postman to test the API endponds
GET: || /api/books/ ||    to get all books
POST:  /api/books/    to get all books    
GET:   /api/books/1/  to get a book by id
PUT:   /api/books/1/   to update a book
DELETE: /api/books/1/  to delete a book

