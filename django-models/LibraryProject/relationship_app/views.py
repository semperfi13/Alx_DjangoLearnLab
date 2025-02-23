from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.utils import timezone


def list_books(request):
    template_name = "relationship_app/list_books.html"
    books = Book.objects.all()
    context = {"books": books}

    return render(request, template_name, context)


class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"
