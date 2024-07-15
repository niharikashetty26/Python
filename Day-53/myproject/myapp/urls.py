# from django.urls import path
# from .views import home, add_book, edit_book, delete_book
#
# urlpatterns = [
#     path('', home, name='home'),
#     path('add/', add_book, name='add_book'),
#     path('edit/<int:pk>/', edit_book, name='edit_book'),
#     path('delete/<int:pk>/', delete_book, name='delete_book'),
#
# ]

# urls.py
# myapp/urls.py
from django.urls import path
from .views import BookListView  # Import your views
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Add this line for home view
    path('books/', BookListView.as_view(), name='book_list'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('books/create/', views.BookCreateView.as_view(), name='book_create'),
    path('books/<int:pk>/update/', views.BookUpdateView.as_view(), name='book_update'),
    path('books/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book_delete'),
]
