from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import login

from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import user_passes_test


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
    form_class = UserCreationForm()
    success_url = reverse_lazy("login")
    template_name = "relationship_app/register.html"


def logout_view(request):
    logout(request)
    return render(request, "registration/logout.html")
    # Redirect to a success page.


def register(request):

    return render(request, "relationship_app/register.html")


def LoginView(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request, "registration/register.html")
    else:
        return render(request, "details not matching")


def is_admin(user):
    user.userprofile.role == "Admin"


def is_librarian(user):
    user.userprofile.role == "Librarian"


def is_member(user):
    user.userprofile.role == "Member"


@user_passes_test(is_admin, login_url="login")
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")


@user_passes_test(is_librarian, login_url="login")
def librarian_view(request):
    return render(request, "relationship_app/librarian_view.html")


@user_passes_test(is_member, login_url="login")
def member_view(request):
    return render(request, "relationship_app/member_view.html")


@permission_required("relationship_app.can_add_book")
def add_book(request):
    return HttpResponse("Add a book.")


@permission_required("relationship_app.can_change_book")
def edit_book(request):
    return HttpResponse("edit a book")


@permission_required("relationship_app.can_delete_book")
def delete_book(request):
    return HttpResponse("Delete a book")
