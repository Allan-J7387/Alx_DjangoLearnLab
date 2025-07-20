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

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.views import View

# Custom view for user registration
class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'relationship_app/register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'relationship_app/register.html', {'form': form})

# You can still use Django's built-in LoginView and LogoutView
