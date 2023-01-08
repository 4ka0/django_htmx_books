from django.urls import path

from .views import BookListView, BookCreateView


urlpatterns = [
    path("", BookListView.as_view(), name="book_list"),
    path("add_book/", BookCreateView.as_view(), name="add_book"),
]
