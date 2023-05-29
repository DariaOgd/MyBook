from django.shortcuts import render,get_object_or_404
from .models import Book
# Create your views here.

def detail(request, pk):
    book = get_object_or_404(Book, pk=pk )
    related_book = Book.objects.filter(category =book.category).exclude(pk=pk)[0:3]


    return render(request, 'book/detail.html', {
        'book':book,
        'related_book' : related_book
    })