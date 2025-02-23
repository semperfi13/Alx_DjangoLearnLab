from django.urls import path
from . import views
from .views import list_books
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path("", views.list_books),
    path("", views.LibraryDetailView.as_view()),
    path("", views.LibrariesView.as_view()),
    path("", views.RegisterView.as_view()),
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
