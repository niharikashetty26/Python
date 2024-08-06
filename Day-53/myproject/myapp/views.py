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

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book
from .forms import BookForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import activate
from django.http import HttpResponse


class CustomLoginView(LoginView):
    template_name = 'myapp/login.html'
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'myapp/signup.html', {'form': form})

def home(request):
    return render(request, 'myapp/home.html')

class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'myapp/book_list.html'
    context_object_name = 'books'
    login_url = '/accounts/login/'

class BookDetailView(DetailView):
    model = Book
    template_name = 'myapp/book_detail.html'
    context_object_name = 'book'

@method_decorator(login_required, name='dispatch')
class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'myapp/book_form.html'
    success_url = reverse_lazy('book_list')

@method_decorator(login_required, name='dispatch')
class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'myapp/book_form.html'
    success_url = reverse_lazy('book_list')

@method_decorator(login_required, name='dispatch')
class BookDeleteView(DeleteView):
    model = Book
    template_name = 'myapp/book_confirm_delete.html'
    success_url = reverse_lazy('book_list')

def test_view(request):
    activate('es')  # Switch to Spanish
    return HttpResponse("Prueba de traducción")