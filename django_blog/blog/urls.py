from django.contrib import admin
from django.urls import path
from .views import RegisterView, profile_view
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import TemplateView
from .views import (
    PostDetailView,
    update_profile,
    UpdateProfileView,
    PostListView,
    PostEditView,
    PostDeleteView,
    PostCreateView,
)

urlpatterns = [
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("profile/", profile_view, name="profile"),
    path(
        "profile/<int:pk>/update/", UpdateProfileView.as_view(), name="profile-update"
    ),
    path("", TemplateView.as_view(template_name="blog/home.html"), name="home"),
    path("login/", LoginView.as_view(template_name="blog/login.html"), name="login"),
    # crud
    path("posts/", PostListView.as_view(), name="posts"),
    path("posts/new", PostCreateView.as_view(), name="posts-new"),
    path("posts/<int:pk>", PostDetailView.as_view(), name="posts-details"),
    path("posts/<int:pk>/edit/", PostEditView.as_view(), name="posts-edit"),
    path("posts/<int:pk>/delete/", PostDeleteView.as_view(), name="posts-delete"),
]
