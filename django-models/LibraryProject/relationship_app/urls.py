from django.urls import path
from . import views
from .views import list_books
from django.contrib.auth.views import LoginView


urlpatterns = [
    path("", list_books),
    path("", views.LibraryDetailView.as_view()),
    path("", views.LibrariesView.as_view()),
    path("", views.RegisterView.as_view()),
    path("", LoginView.as_view()),
]
