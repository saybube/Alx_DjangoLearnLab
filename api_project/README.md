# Django API Project: Book Management

## Authentication & Permissions
This API is secured using **Django REST Framework Token Authentication**.

### How to access:
1. **Obtain a Token**: Send a POST request to `/api-token-auth/` with your username and password.
2. **Use the Token**: Include the token in the HTTP Authorization header for all requests to `/api/books_all/`.
   - Header: `Authorization: Token <your_token_key>`

### Permission Levels:
- **Authenticated Users**: Full access to List, Create, Retrieve, Update, and Delete books.
- **Unauthenticated Users**: Blocked with a `401 Unauthorized` response.