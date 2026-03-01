from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import ExampleForm

# Create your views here.
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    """
    Securely list and search books using Django ORM and Forms.
    Uses Django's ORM and Form validation to sanitize input.
    The ORM parameterizes queries, which is a primary defense against SQL Injection.
    """
    books = Book.objects.all()
    form = ExampleForm(request.GET)

    if form.is_valid():
        title_query = form.cleaned_data.get('title')
        author_query = form.cleaned_data.get('author')
        
        if title_query:
            books = books.filter(title__icontains=title_query)
        if author_query:
            books = books.filter(author__icontains=author_query)

    return render(request, 'bookshelf/book_list.html', {'books': books, 'form': form})

def form_example_view(request):
    form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    pass

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    pass

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    pass

