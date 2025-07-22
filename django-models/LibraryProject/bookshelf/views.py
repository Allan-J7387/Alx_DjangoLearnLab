from django.shortcuts import render
from .models import Book

def list_books(request):
    books = Book.objects.all()  # ✅ Required: Use Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})  # ✅ Required path
