from django.forms import ModelForm
from .models import Book


class AddBookForm(ModelForm):

    class Meta:
        model = Book
        fields = ['title', 'author', 'price']
