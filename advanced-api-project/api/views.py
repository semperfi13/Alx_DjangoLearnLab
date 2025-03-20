from django.shortcuts import render
from rest_framework import generics
from .serializers import BookSerializer
from .models import Book
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as Filters


class BookFilter(Filters.FilterSet):
    title = Filters.CharFilter()
    author = Filters.CharFilter()
    publication_year = Filters.CharFilter()

    class Meta:
        model = Book
        fields = ["title", "author", "publication_year"]


class CustomBookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filterset_class = BookFilter
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]
    search_fields = ["title", "author"]
    ordering_fields = ["title", "publication_year"]
    ordering = ["title"]


class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class DetailView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class UpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class DeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer
