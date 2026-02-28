book.delete()
all_books = Book.objects.all()
print(all_books)
# Expected Output: <QuerySet []>