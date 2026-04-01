from django.urls import path
from books import views


urlpatterns = [
    path('books/', views.ListBookView.as_view(), name = 'books_list'),
    # path('books/', views.list_books_view, name = 'index')
]