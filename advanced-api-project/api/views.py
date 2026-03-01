from django.shortcuts import render
from rest_framework import generics
from django_filters import rest_framework as filters
from rest_framework import filters as drf_filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer

# Create your views here.

# Anyone can view the list of books, but only logged-in users can post.
class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [
        filters.DjangoFilterBackend, 
        drf_filters.SearchFilter,    
        drf_filters.OrderingFilter   
    ]

    # CONFIGURING THE FILTERABLE FIELDS
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author__name'] 
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']

# Detail view for a single book.
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Explicit CreateView with strict authentication.
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

# Explicit UpdateView with strict authentication.
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

# Explicit DeleteView with strict authentication.
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]