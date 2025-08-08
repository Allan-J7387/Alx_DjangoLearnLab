from rest_framework.routers import DefaultRouter
from .views import AuthorViewSet, BookViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView
)

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    
    # ✅ These two need to explicitly include 'books/update' and 'books/delete'
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),
]
