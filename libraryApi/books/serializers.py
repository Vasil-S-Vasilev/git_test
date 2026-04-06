from rest_framework import serializers

from books.models import Book, Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = '__all__'

    def create(self, validated_data):

        authors = validated_data.pop('author')
        authors_names = [a['name'] for a in authors]
  
        book = Book.objects.create(**validated_data)  # queryset of 1 book object

        existing_object_authors = Author.objects.filter(name__in=authors_names)  # queryset of objects <QuerySet[<Author: Dido>]>
        existing_authors_names = set(existing_object_authors.values_list('name', flat=True)) # queryset of string <QuerySet['Dido']>

        new_authors_names = set(authors_names) - existing_authors_names
        new_object_authors = [Author(name=a_name) for a_name in new_authors_names]
  
        created_object_authors = Author.objects.bulk_create(new_object_authors)
        
        all_object_authors = list(existing_object_authors) + list(created_object_authors)

        book.author.set(all_object_authors)

        return book




