from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),   # ✅ uses path()
]
: ["BookList.as_view"]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# Router setup
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Keep the simple ListAPIView route
    path('books/', BookList.as_view(), name='book-list'),

    # Add router-generated CRUD routes
    path('', include(router.urls)),
]
