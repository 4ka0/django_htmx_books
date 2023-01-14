from django.views.generic import ListView
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http.response import HttpResponse

from .models import Book
from .forms import BookForm


class BookListView(ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "base.html"


@require_http_methods(['POST'])
def create_book(request):
    form = BookForm(request.POST)
    if form.is_valid:
        book = form.save()
    return render(request, 'partial_individual_book.html', {'book': book})


@require_http_methods(['DELETE'])
def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return HttpResponse()


@require_http_methods(['PUT'])
def update_read_status(request, pk):
    book = Book.objects.get(pk=pk)
    if book.read:
        book.read = False
    else:
        book.read = True
    book.save()
    return render(request, 'partial_individual_book.html', {'book': book})


def update_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save()
            return render(request, 'partial_individual_book.html', {'book': book})
    else:
        form = BookForm(instance=book)
    return render(request, 'partial_individual_book_update_form.html', {'book': book, 'form': form})


def get_book(request, pk):
    book = Book.objects.get(pk=pk)
    return render(request, 'partial_individual_book.html', {'book': book})
