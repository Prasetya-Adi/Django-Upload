from typing import List
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.core.files.storage import FileSystemStorage
from django.views.generic import ListView, FormView, CreateView

from .forms import BookForm
from .models import Book

# Create your views here.


def index(request):
    return render(request, 'upload/index.html')


def upload(request):
    contex = {}
    if request.method == 'POST':
        UploadedFile = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(UploadedFile.name, UploadedFile)
        contex['url'] = fs.url(name)
    return render(request, 'upload/upload.html', contex)

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
