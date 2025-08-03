from django.urls import path
from .views import BookList

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]



from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Original ListAPIView
    path('books/', BookList.as_view(), name='book-list'),

    # Routes handled by the router for CRUD operations
    path('', include(router.urls)),
]


from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('auth/token/', obtain_auth_token, name='api_token_auth'),  # ✅ Token endpoint
    path('', include(router.urls)),
]
