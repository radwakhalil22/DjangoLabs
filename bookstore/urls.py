from django.shortcuts import render
from django.http import HttpResponse
# from .views import index
from .views import create_book, index, books_list, book_detail, book_delete, book_update

from django.urls import path
app_name = 'bookstore'
urlpatterns = [
    path('', books_list,name='index'),
    path('book_list/', books_list, name="book-list"),
    path('<int:pk>/detail', book_detail, name="book-detail"),
    path('<int:pk>/delete', book_delete, name="book-delete"),
    path('<int:pk>/update', book_update, name="book-update"),
    path('create', create_book, name="book-create"),
]
