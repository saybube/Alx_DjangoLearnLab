from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITests(APITestCase):

    def setUp(self):
        """Set up a user, author, and an initial book for every test"""
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.author = Author.objects.create(name="J.K. Rowling")
        self.book = Book.objects.create(
            title="Harry Potter", 
            publication_year=1997, 
            author=self.author
        )
        # URLs from your urls.py names
        self.list_url = reverse('book-list')
        self.create_url = reverse('book-create')
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book.pk})
        self.update_url = reverse('book-update', kwargs={'pk': self.book.pk})
        self.delete_url = reverse('book-delete', kwargs={'pk': self.book.pk})

    def get_results(self, response_data):
        """Helper to handle both paginated and non-paginated responses"""
        if isinstance(response_data, dict) and 'results' in response_data:
            return response_data['results']
        return response_data

    # --- CRUD Scenarios ---

    def test_create_book(self):
        """Test: Creating a Book and ensuring data is saved"""
        self.client.login(username='testuser', password='password123')
        data = {"title": "The Hobbit", "publication_year": 1937, "author": self.author.id}
        response = self.client.post(self.create_url, data)
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(title="The Hobbit").publication_year, 1937)

    def test_update_book(self):
        """Test: Updating a Book and verifying changes"""
        self.client.login(username='testuser', password='password123')
        updated_data = {"title": "Harry Potter & The Phoenix", "publication_year": 2003, "author": self.author.id}
        response = self.client.put(self.update_url, updated_data)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Harry Potter & The Phoenix")

    def test_delete_book(self):
        """Test: Deleting a Book and ensuring it is removed"""
        self.client.login(username='testuser', password='password123')
        response = self.client.delete(self.delete_url)
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    # --- Permission & Security Scenarios ---

    def test_unauthenticated_creation_fails(self):
        """Test: Ensure unauthenticated users cannot create books (Security check)"""
        data = {"title": "Ghost Book", "publication_year": 2024, "author": self.author.id}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # --- Query Capabilities Scenarios ---

    def test_search_functionality(self):
        """Test: Keyword search for 'Harry'"""
        response = self.client.get(f"{self.list_url}?search=Harry")
        results = self.get_results(response.data)
        
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['title'], "Harry Potter")

    def test_ordering_functionality(self):
        """Test: Ordering by publication_year"""
        # Create an older book
        Book.objects.create(title="Old Book", publication_year=1900, author=self.author)
        
        response = self.client.get(f"{self.list_url}?ordering=publication_year")
        results = self.get_results(response.data)
        
        # 'Old Book' (1900) should come before 'Harry Potter' (1997)
        self.assertEqual(results[0]['title'], "Old Book")

    