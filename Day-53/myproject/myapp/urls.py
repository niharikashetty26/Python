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
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView, signup, CustomLoginView

urlpatterns = [
    path('', BookListView.as_view(), name='book_list'),
    path('<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('create/', BookCreateView.as_view(), name='book_create'),
    path('<int:pk>/update/', BookUpdateView.as_view(), name='book_update'),
    path('<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
    path('signup/', signup, name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
]

