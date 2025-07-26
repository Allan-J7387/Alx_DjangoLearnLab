from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    # Add other views here
]

from django.urls import path
from .views import admin_view, librarian_view, member_view

urlpatterns = [
    path('admin-dashboard/', admin_view.admin_view, name='admin_view'),
    path('librarian-dashboard/', librarian_view.librarian_view, name='librarian_view'),
    path('member-dashboard/', member_view.member_view, name='member_view'),
    # Include auth and registration paths as well
]

from django.urls import path
from . import views

urlpatterns = [
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
]



from django.urls import path
from .views import list_books, LibraryDetailView  # ✅ Required for check

urlpatterns = [
    path('books/', list_books, name='list_books'),  # Function-based view
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Class-based view
]
