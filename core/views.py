from django.shortcuts import render
from book.models import Category, Book
# Create your views here.
def index(request):
    book = Book.objects.filter()[0:6]
    categories = Category.objects.all()
    return render(request, 'index.html', {
        'categories' : categories,
        'book' : book,
    })