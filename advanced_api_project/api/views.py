from rest_framework import viewsets
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# ListView - Retrieve all books
class BookListView(generics.ListAPIView):
    """
    GET: Returns a list of all books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Publicly accessible


# DetailView - Retrieve a single book
class BookDetailView(generics.RetrieveAPIView):
    """
    GET: Returns a single book by ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Publicly accessible


# CreateView - Add a new book (auth required)
class BookCreateView(generics.CreateAPIView):
    """
    POST: Create a new book entry.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Auth required


# UpdateView - Modify a book (auth required)
class BookUpdateView(generics.UpdateAPIView):
    """
    PUT/PATCH: Update a book entry.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Auth required


# DeleteView - Delete a book (auth required)
class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE: Remove a book by ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Auth required


permission_classes = [IsOwnerOrReadOnly]
