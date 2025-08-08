from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

# Serializer for the Book model.
# Validates that the publication year is not in the future.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

# Serializer for the Author model.
# Includes a nested BookSerializer to serialize all related books.
class AuthorSerializer(serializers.ModelSerializer):
    # Nested serializer to serialize related books dynamically.
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
