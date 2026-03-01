API View Documentation
Endpoints and Access Control
List Books

URL: /api/books/

Method: GET

Permission: AllowAny (Public)

Description: Retrieves a complete list of all books in the database.

Create Book

URL: /api/books/

Method: POST

Permission: IsAuthenticated (Logged-in users only)

Description: Allows an authenticated user to add a new book record.

Retrieve Book Details

URL: /api/books/<int:pk>/

Method: GET

Permission: AllowAny (Public)

Description: Returns detailed information for a single book identified by its ID.

Update Book

URL: /api/books/update/<int:pk>/

Method: PUT / PATCH

Permission: IsAuthenticated (Logged-in users only)

Description: Allows an authenticated user to modify an existing book's details.

Delete Book

URL: /api/books/delete/<int:pk>/

Method: DELETE

Permission: IsAuthenticated (Logged-in users only)

Description: Permanently removes a book record from the system.

Custom Configurations & Hooks
Permissions Strategy: We implemented a "Public to Read, Private to Write" model. By using IsAuthenticatedOrReadOnly and explicit IsAuthenticated classes, we protect the integrity of the data while keeping the information accessible to the public.

Method Overriding: The perform_create hook was included in the BookCreateView. This allows for future extensibility, such as automatically linking a book to the user who created the entry or triggering external notifications upon a successful save.

Generic View Utilization: We leveraged Django REST Framework’s generics library to ensure the API follows standard RESTful patterns, reducing code complexity and improving maintainability.