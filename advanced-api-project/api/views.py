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



from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    """
    GET: Returns a list of all books.
    Supports:
    - Filtering by title, author ID, publication year.
    - Searching by title and author's name.
    - Ordering by title or publication year.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

    # Filtering, searching, ordering
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]

    # Fields available for filtering
    filterset_fields = ['title', 'author', 'publication_year']

    # Fields available for full-text search
    search_fields = ['title', 'author__name']

    # Fields available for ordering
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default ordering
