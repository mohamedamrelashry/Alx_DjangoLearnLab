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
from django.urls import path
from . import views

urlpatterns = [
    path("admin-role/", views.admin_view, name="admin_view"),
    path("librarian-role/", views.librarian_view, name="librarian_view"),
    path("member-role/", views.member_view, name="member_view"),
]
# relationship_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("books/add/", views.add_book, name="add_book"),
    path("books/<int:pk>/edit/", views.edit_book, name="edit_book"),
    path("books/<int:pk>/delete/", views.delete_book, name="delete_book"),
]
