from django.views.generic import ListView, CreateView

from .models import Book
from .forms import AddBookForm


class BookListView(ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "book_list.html"


class BookCreateView(CreateView):
    model = Book
    form_class = AddBookForm
    template_name = "_base.html"
