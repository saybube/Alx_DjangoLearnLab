from django.contrib import admin
from .models import Book

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Display these fields in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add a search bar for title and author
    search_fields = ('title', 'author')
    
    # Add a filter sidebar for publication year
    list_filter = ('publication_year',)

