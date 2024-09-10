from django.shortcuts import render, get_object_or_404, redirect
from .models import Book


def book_list(request):
    books = Book.objects.all()
    ctx = {"boks": books}
    return render(request, 'list.html', ctx)


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'detail.html', {'book': book})

