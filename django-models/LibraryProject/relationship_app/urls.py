from django.urls import path
from . import views
from .views import list_books
urlpatterns = [
    path('books/', views.list_books, name='list_books'),  
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('relationship_app.urls')),  # include app urls
]
views.register", "LogoutView.as_view(template_name=", "LoginView.as_view(template_name="]
