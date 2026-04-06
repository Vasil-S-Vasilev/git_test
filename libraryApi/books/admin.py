from django.contrib import admin
from books.models import Book, Publisher
from books.models import Author


# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    filter_horizontal = ('author',)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    pass