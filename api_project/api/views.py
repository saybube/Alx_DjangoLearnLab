from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer

# Create your views here.
class BookList(generics.ListAPIView):
   queryset = Book.objects.all()
   serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    ViewSet for viewing and editing book instances.
    
    Authentication:
    - Requires TokenAuthentication or SessionAuthentication.
    
    Permissions:
    - IsAuthenticated: Only users who are logged in and provide 
      a valid token/session can access CRUD operations.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    permission_classes = [IsAuthenticated]