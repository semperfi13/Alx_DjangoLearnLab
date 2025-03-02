from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from .models import Book
from .forms import ExampleForm
from django.http import HttpResponseRedirect

# Create your views here.


def my_view(request):
    pass


@login_required
@permission_required("bookshelf.can_view", raise_exception=True)
def book_list(request):
    template_name = "bookshelf/list_books.html"
    books = Book.objects.all()
    context = {"books": books}

    return render(request, template_name, context)


def get_name(request):
    template_name = "bookshelf/form_example.html"
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = ExampleForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/thanks/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ExampleForm()

    return render(request, template_name, {"form": form})
