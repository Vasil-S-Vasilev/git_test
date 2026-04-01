from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from books.models import Book
from books.serializers import BookSerializer
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET' ,'POST'])
def list_books_view(request):
    if request.method == 'GET':
        books = Book.objects.all()

        serializer = BookSerializer(books, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

