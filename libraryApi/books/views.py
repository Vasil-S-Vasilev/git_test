from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from books.models import Book
from books.serializers import BookSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView


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


class ListBookView(APIView):  # APIView is the base class, same as View in CBV

    def get(self, request):
        if request.method == 'GET':
            books = Book.objects.all()

            serializer = BookSerializer(books, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK) 

    def post(self, request):
        serializer = BookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# with Generic Api View
class ListBooksApiView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
