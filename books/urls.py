from django.urls import path

from .views import (
    BookListView, create_book, delete_book, update_read_status, update_book, get_book
)


urlpatterns = [
    path("", BookListView.as_view(), name="book_list"),
    path("create_book/", create_book, name="create_book"),
    path("delete_book/<int:pk>/", delete_book, name="delete_book"),
    path("update_read_status/<int:pk>/", update_read_status, name="update_read_status"),
    path("update_book/<int:pk>/", update_book, name="update_book"),
    path("get_book/<int:pk>/", get_book, name="get_book"),
]
