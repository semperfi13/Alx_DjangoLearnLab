from django.urls import path
from . import views
from .views import list_books

urlpatterns = [
    path("", list_books),
    path("", views.LibraryDetailView.as_view()),
]
