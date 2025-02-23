from django.urls import path
from . import views
from .views import LibraryView

urlpatterns = [
    path("", views.bookView),
    path("/library", LibraryView.as_view()),
]
