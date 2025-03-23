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
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
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
    # CRUD for posts
    path("posts/", PostListView.as_view(), name="posts"),
    path("post/new/", PostCreateView.as_view(), name="posts-new"),
    path("post/<int:pk>", PostDetailView.as_view(), name="posts-details"),
    path("post/<int:pk>/update/", PostEditView.as_view(), name="posts-edit"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="posts-delete"),
    # CRUD for comments
    path(
        "post/<int:pk>/comments/new/",
        CommentCreateView.as_view(),
        name="comment-update",
    ),
    path(
        "comment/<int:pk>/update/", CommentUpdateView.as_view(), name="comment-update"
    ),
    path(
        "comment/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment-delete"
    ),
]
