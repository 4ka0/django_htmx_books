from django.views.generic import ListView

from .models import Book


class BookListView(ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "index.html"
