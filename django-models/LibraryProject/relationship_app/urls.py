from django.urls import path
from . import views
from .views import BookView

urlpatterns = [
    path("", views.bookView),
    path("/library", BookView.as_view()),
]
