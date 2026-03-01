# Social Media API Documentation

This project provides a backend REST API for a social media platform, built using Django and the Django REST Framework (DRF). The system handles user authentication, profile management, and social relationship tracking.

---

## Technical Overview: User Model
The application implements a **Custom User Model** by extending Django's `AbstractUser`. This approach provides the flexibility required for social media features while maintaining compatibility with Django’s built-in authentication system.

### Custom Fields
| Field | Type | Description |
| :--- | :--- | :--- |
| `bio` | TextField | Stores user biographical information (optional). |
| `profile_picture` | ImageField | Stores user avatar images in the `profile_pics/` directory. |
| `followers` | ManyToManyField | A self-referential relationship used to track user connections (symmetrical=False). |



---

## Installation and Environment Setup

### 1. Repository Configuration
Navigate to the project directory and initialize the environment:
```bash
python -m venv venv
source venv/Scripts/activate 

API Architecture and Authentication
The API utilizes Token-based Authentication. Authenticated requests must include the header:
Authorization: Token <your_token_key>

Endpoints Guide
1. Accounts & Authentication
2. Posts (CRUD)
Base URL: /api/posts/

List Posts (with Pagination & Search):
GET /api/posts/?search=keyword&ordering=-created_at
Response: Returns a paginated list of posts.

Create Post:
POST /api/posts/
Payload: {"title": "My Title", "content": "My Content"}
Note: Author is automatically assigned to the logged-in user.

3. Comments (CRUD)
Base URL: /api/comments/

Create Comment:
POST /api/comments/
Payload: {"post": 1, "content": "This is a comment"}

Edit/Delete:
PATCH /api/comments/<id>/ | DELETE /api/comments/<id>/
Permission: Only the original author can edit or delete.

Examples
Create Post Request (POST)
URL: http://127.0.0.1:8000/api/posts/
Header: Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b

Success Response (201 Created)
Development Standards
Framework: Django 5.x

Filtering: Django-filter with SearchFilter and OrderingFilter

Pagination: PageNumberPagination (10 items per page)