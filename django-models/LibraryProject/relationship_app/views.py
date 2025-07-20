from django.shortcuts import render
from .models import Book

# Function-based view to list all books
def list_books_view(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

from django.views.generic.detail import DetailView
from .models import Library

# Class-based view for library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
