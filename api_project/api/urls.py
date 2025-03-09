from .views import BookList
from django.urls import path, include
from .views import BookViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"books_all", BookViewSet, basename="book_all")
urlpatterns = [
    path("", BookList.as_view(), name="book-list"),  # Maps to the BookList view
    # Include the router URLs for BookViewSet (all CRUD operations)
    # This includes all routes registered with the router
    path("", include(router.urls)),
]
