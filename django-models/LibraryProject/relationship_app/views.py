from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Library
from django.views.generic import TemplateView


def bookView(request):
    template_name = "relationship_app/book_list.html"

    return HttpResponse("Hello", template_name)


class BookView(TemplateView):

    def get(self, request):
        template_name = "relationship_app/library_detail.html"
        library = Library.objects.get(id="1")
        context = {"library": library}
        return render(request, template_name, context)
