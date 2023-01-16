from django.urls import path

from .views import (
    book_detail,
    book_list,
    book_list_sort_title,
    book_list_sort_author,
    book_list_sort_price,
    book_list_sort_status,
    create_book,
    delete_book,
    update_book_status,
    update_book_details,
)


urlpatterns = [
    path("", book_list, name="book_list"),
    path("book_list_sort_title/<direction>/", book_list_sort_title, name="book_list_sort_title"),
    path("book_list_sort_author/<direction>/", book_list_sort_author, name="book_list_sort_author"),
    path("book_list_sort_price/<direction>/", book_list_sort_price, name="book_list_sort_price"),
    path("book_list_sort_status/<direction>/", book_list_sort_status, name="book_list_sort_status"),
    path("book_detail/<int:pk>/", book_detail, name="book_detail"),
    path("create_book/", create_book, name="create_book"),
    path("delete_book/<int:pk>/", delete_book, name="delete_book"),
    path("update_book_status/<int:pk>/", update_book_status, name="update_book_status"),
    path("update_book_details/<int:pk>/", update_book_details, name="update_book_details"),
]
