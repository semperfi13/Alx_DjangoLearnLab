from django.shortcuts import render
from .serializers import BookSerializer
from rest_framework import generics
from rest_framework import viewsets
from .models import Book
from rest_framework.permissions import IsAuthenticated, AllowAny

# Create your views here.


class BookList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
