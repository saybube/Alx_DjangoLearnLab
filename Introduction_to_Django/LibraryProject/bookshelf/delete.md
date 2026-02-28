from bookshelf.models import Book

book.delete()
all_books = Book.objects.all()
print(all_books)
# Expected Output: <QuerySet []>