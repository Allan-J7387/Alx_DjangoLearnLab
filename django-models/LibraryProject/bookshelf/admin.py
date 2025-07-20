from django.contrib import admin
from .models import Book

# Custom admin configuration for Book
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Show these columns in list view
    list_filter = ('author', 'publication_year')            # Add filtering by author and year
    search_fields = ('title', 'author')                     # Enable search by title and author
