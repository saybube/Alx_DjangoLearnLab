import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def query_all_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    print(f"Books by {author_name}:")
    for book in books:
        print(f"- {book.title}")
    return books

def list_all_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    print(f"\nBooks in {library_name} library:")
    for book in books:
        print(f"- {book.title}")
    return books

def retrieve_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    print(f"\nLibrarian for {library_name}: {librarian.name}")
    return librarian

if __name__ == "__main__":
    pass
    