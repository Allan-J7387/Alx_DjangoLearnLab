from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book, Library  # ✅ Contains: "from .models import Library"

# Function-based view for listing books
def list_books_view(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view for displaying library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  # ✅ Contains: "relationship_app/library_detail.html"
    context_object_name = 'library'                         # ✅ Contains: "library"
