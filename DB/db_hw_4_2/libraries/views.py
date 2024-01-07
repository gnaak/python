from django.shortcuts import render, redirect
from .models import Book, Review
from .forms import BookForm, ReviewForm
# Create your views here.

def index(request):
    books = Book.objects.all()
    context = {
        'books':books,
    }
    return render(request, 'libraries/index.html', context)


def detail(request, pk):
    book = Book.objects.get(pk=pk)
    review_form = ReviewForm()
    reviews = book.review_set.all()
    context = {
        'book':book,
        'review_form': review_form,
        'reviews': reviews,
    }
    return render(request, 'libraries/detail.html', context)

def create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            # article.user에 현재 로그인된 유저 저장 
            book.user = request.user
            form.save()
            return redirect('libraries:detail', book.pk)
    else:
        form = BookForm()
    context = {
        'form': form,
    }
    return render(request, 'libraries/create.html', context)

def delete(request, pk):
    book = Book.objects.get(pk=pk)
    if request.user == book.user:
        book.delete()
    return redirect('libraries:index')