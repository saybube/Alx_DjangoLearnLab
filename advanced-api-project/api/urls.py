from django.urls import path
from .views import (
    BookListView, 
    BookDetailView, 
    BookCreateView, 
    BookUpdateView, 
    BookDeleteView
)

urlpatterns = [
    # 1. List View: Retrieve all books
    path('books/', BookListView.as_view(), name='book-list'),

    # 2. Detail View: Retrieve a single book by its primary key (ID)
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    # 3. Create View: Add a new book
    path('books/create/', BookCreateView.as_view(), name='book-create'),

    # 4. Update View: Edit an existing book
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),

    # 5. Delete View: Remove a book from the database
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),
]