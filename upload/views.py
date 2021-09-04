
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView

from .forms import BookForm
from .models import Book

# Create your views here.


def index(request):
    return render(request, 'upload/index.html')


# FUNCTION Based View


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book/function/book-list.html', {
        'books': books
    })


def book_upload(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('function-book-list')
    else:
        form = BookForm()
    return render(request, 'book/function/book-upload.html', {
        'form': form
    })


def book_delete(request, pk):
    if request.method == 'POST':
        book = Book.objects.get(pk=pk)
        book.delete()
    return redirect('function-book-list')


# CLASS Based View

class book_list_view(ListView):
    model = Book
    template_name = "book/class/book-list.html"


class book_upload_view(CreateView):
    form_class = BookForm
    template_name = "book/class/book-upload.html"
    success_url = reverse_lazy('class-book-list')
