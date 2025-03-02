from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from .models import Book

# Create your views here.


def my_view(request):
    pass


@login_required
@permission_required("bookshelf.can_view", raise_exception=True)
def list_books(request):
    template_name = "relationship_app/list_books.html"
    books = Book.objects.all()
    context = {"books": books}

    return render(request, template_name, context)
