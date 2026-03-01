from rest_framework import serializers
from .models import Author, Book
from datetime import date

# BookSerializer handles the conversion of Book model instances into JSON format.
# It includes a custom validation rule for the publication year.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    
    # Custom Validation: Ensure publication_year is not in the future
    # DRF automatically calls this method during the is_valid() process.
    def validate_publication_year(self, value):
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("The publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    # Nested Serializer: Links the 'books' related_name from the Model
    books = BookSerializer(many=True, read_all=True)

    class Meta:
        model = Author
        fields = ['name', 'books']