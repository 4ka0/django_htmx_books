from django.views.generic import ListView
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http.response import HttpResponse

from .models import Book
from .forms import CreateBookForm


class BookListView(ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "base.html"


@require_http_methods(['POST'])
def create_book(request):
    form = CreateBookForm(request.POST)
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
