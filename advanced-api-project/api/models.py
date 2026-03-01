from django.db import models

# Create your models here.
# The Author model represents the creator of a literary work.
# It serves as the 'One' in our One-to-Many relationship.
class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
# The Book model represents individual titles.
# It contains a Foreign Key to Author, meaning each book is linked to exactly one author,
# but one author can have multiple books.
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    # One-to-Many: One Author can have many Books
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return f"{self.title} ({self.publication_year})"