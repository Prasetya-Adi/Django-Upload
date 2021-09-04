from django import forms
from django.forms import fields

from .models import Book, Book_Class, Book_Function


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'pdf', 'cover')


class BookForm_Function(forms.ModelForm):
    class Meta:
        model = Book_Function
        fields = ('title', 'author', 'pdf', 'cover')


class BookForm_Class(forms.ModelForm):
    class Meta:
        model = Book_Class
        fields = ('title', 'author', 'pdf', 'cover')
