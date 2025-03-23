from django.contrib import admin
from django.urls import path
from .views import RegisterView, profile_view
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import TemplateView
from .views import UpdateProfileView, update_profile

urlpatterns = [
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("profile/", profile_view, name="profile"),
    path("profile/<int:pk>/update/", update_profile, name="profile-update"),
    path("", TemplateView.as_view(template_name="blog/home.html"), name="home"),
    path("login/", LoginView.as_view(template_name="blog/login.html"), name="login"),
]
