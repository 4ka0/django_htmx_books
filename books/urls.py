from django.urls import path

from .views import (
    book_list,
    book_list_sort_title,
    book_detail,
    create_book,
    delete_book,
    update_book_details,
    update_book_status
)


urlpatterns = [
    path("", book_list, name="book_list"),
    path(
        "book_list_sort_title/<direction>/",
        book_list_sort_title,
        name="book_list_sort_title"
    ),
    path("book_detail/<int:pk>/", book_detail, name="book_detail"),
    path("create_book/", create_book, name="create_book"),
    path("delete_book/<int:pk>/", delete_book, name="delete_book"),
    path("update_book_status/<int:pk>/", update_book_status, name="update_book_status"),
    path("update_book_details/<int:pk>/", update_book_details, name="update_book_details"),
]
