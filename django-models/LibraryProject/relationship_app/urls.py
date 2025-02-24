from django.urls import path
from . import views
from .views import list_books
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path("", views.list_books),
    path("", views.LibraryDetailView.as_view()),
    path("admin/", views.admin_view, name="admin"),
    path("", views.LibrariesView.as_view()),
    path("add_book/", views.add_book, name="add_book"),
    path("edit_book/", views.add_book, name="add_book"),
    path("delete_book/", views.add_book, name="add_book"),
    path("librarian/", views.librarian_view, name="librarian"),
    path("member/", views.member_view, name="member"),
    path("", views.register),
    path(
        "",
        LoginView.as_view(template_name="relationship_app/login.html"),
        name="login",
    ),
    path(
        "",
        LogoutView.as_view(template_name="relationship_app/logout.html"),
        name="logout",
    ),
]
