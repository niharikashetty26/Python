# from django.shortcuts import render, get_object_or_404, redirect
# from .models import Book
# from .forms import BookForm
#
#
# def create_book(request):
#     if request.method == 'POST':
#         form = BookForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('book_list')
#     else:
#         form = BookForm()
#     return render(request, 'myapp/book_form.html', {'form': form})
#
#
# def update_book(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     if request.method == 'POST':
#         form = BookForm(request.POST, instance=book)
#         if form.is_valid():
#             form.save()
#             return redirect('book_list')
#     else:
#         form = BookForm(instance=book)
#     return render(request, 'myapp/book_form.html', {'form': form})
#
#
# def delete_book(request, pk):
#     book = get_object_or_404(Book, pk=pk)
#     if request.method == 'POST':
#         book.delete()
#         return redirect('book_list')
#     return render(request, 'myapp/book_confirm_delete.html', {'book': book})
#
#
# def list_books(request):
#     books = Book.objects.all()
#     return render(request, 'myapp/book_list.html', {'books': books})


from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book
from .forms import BookForm
from django.shortcuts import render

def home(request):
    return render(request, 'myapp/home.html')

class BookListView(ListView):
    model = Book
    template_name = 'myapp/book_list.html'
    context_object_name = 'books'


class BookDetailView(DetailView):
    model = Book
    template_name = 'myapp/book_detail.html'
    context_object_name = 'book'


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'myapp/book_form.html'
    success_url = reverse_lazy('book_list')


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'myapp/book_form.html'
    success_url = reverse_lazy('book_list')


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'myapp/book_confirm_delete.html'
    success_url = reverse_lazy('book_list')
