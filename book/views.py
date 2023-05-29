from django.shortcuts import render,get_object_or_404, redirect

from .models import Book
from .forms import NewBookForm
# Create your views here.

def detail(request, pk):
    book = get_object_or_404(Book, pk=pk )
    related_book = Book.objects.filter(category =book.category).exclude(pk=pk)[0:3]


    return render(request, 'book/detail.html', {
        'book':book,
        'related_book' : related_book
    })


def new(request):
    form = NewBookForm()

    if request.method == 'POST':
        form = NewBookForm(request.POST, request.FILES)

        if form.is_valid():
            book = form.save(commit=False)
            book.save()

            return redirect('book:detail', pk=book.id)
    else:
        form = NewBookForm()

    return render(request, 'book/form.html',{
        'form':form,
        'title': 'New book',
    })

