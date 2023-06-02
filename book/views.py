from django.shortcuts import render,get_object_or_404, redirect
from django.db.models import Q
from .models import Book, Category
from .forms import NewBookForm,EditBookForm
# Create your views here.


def books(request):
    books = Book.objects.filter()
    query = request.GET.get('query', '')
    categories = Category.objects.all()
    category_id = request.GET.get('category', 0)


    if query:
        books = books.filter(Q(name__icontains=query) | Q(author__icontains = query))

    if category_id:
        books= books.filter(category_id = category_id)

    return render(request,'book/books.html', {
        'books':books,
        'query':query,
        'categories': categories,
        'category_id': int(category_id),
    })




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




def delete(request,pk):
    book = get_object_or_404(Book,pk=pk)
    book.delete()

    return redirect('index')


def edit(request,pk):
    book = get_object_or_404(Book,pk=pk)
    form = NewBookForm()

    if request.method == 'POST':
        form = EditBookForm(request.POST, request.FILES,instance=book)

        if form.is_valid():
           
            book.save()

            return redirect('book:detail', pk=book.id)
    else:
        form = EditBookForm(instance=book)

    return render(request, 'book/form.html',{
        'form':form,
        'title': 'Edit book',
    })
