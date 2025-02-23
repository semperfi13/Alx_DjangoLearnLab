from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth import login


def list_books(request):
    template_name = "relationship_app/list_books.html"
    books = Book.objects.all()
    context = {"books": books}

    return render(request, template_name, context)


class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"


class LibrariesView(ListView):
    model = Library
    template_name = "relationship_app/list_libraries.html"
    context_object_name = "libraries"


class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "relationship_app/register.html"


def logout_view(request):
    logout(request)
    # Redirect to a success page.


def register(request):

    return render(request, "relationship_app/register.html")
