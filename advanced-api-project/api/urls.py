from django.contrib import admin
from django.urls import path
from .views import CustomBookListView, CreateView, DetailView, UpdateView

urlpatterns = [
    path("books/", CustomBookListView.as_view(), name="books"),
    path("books/create", CreateView.as_view(), name="books-create"),
    path("books/retrieve/<pk>/", DetailView.as_view(), name="books-create"),
    path("books/update/<pk>/", UpdateView.as_view(), name="books-update"),
    path("books/delete/<pk>/", UpdateView.as_view(), name="books-delete"),
]
