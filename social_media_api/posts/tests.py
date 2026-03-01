from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import Post

User = get_user_model()
# Create your tests here.
class PostAPITests(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='password123')
        self.user2 = User.objects.create_user(username='user2', password='password123')
        self.post = Post.objects.create(author=self.user1, title="User1's Post", content="Hello")
        self.url = reverse('post-detail', kwargs={'pk': self.post.pk})

    def test_delete_post_permission(self):
        """Test that a user cannot delete another user's post."""
        # Log in as user2
        self.client.force_authenticate(user=self.user2)
        response = self.client.delete(self.url)
        
        # Should be forbidden
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue(Post.objects.filter(pk=self.post.pk).exists())

    def test_create_post_authenticated(self):
        """Test creating a post automatically assigns the author."""
        self.client.force_authenticate(user=self.user1)
        data = {'title': 'New Post', 'content': 'Content here'}
        response = self.client.post(reverse('post-list'), data)
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['author'], self.user1.username)