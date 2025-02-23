from django.urls import path
from . import views

urlpatterns = [
    path("", views.bookView),
    path("", views.LibraryView.as_view()),
]
