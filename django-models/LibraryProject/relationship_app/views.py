from django.shortcuts import render
from .models import Book
from .models import Library

from django.views.generic import TemplateView


def bookView(request):
    template_name = "relationship_app/list_books.html"
    books = Book.objects.all()
    context = {"books": books}

    return render(request, template_name, context)


class LibraryView(TemplateView):

    def get(self, request):
        template_name = "relationship_app/library_detail.html"
        library = Library.objects.get(id="1")
        context = {"library": library}
        return render(request, template_name, context)
