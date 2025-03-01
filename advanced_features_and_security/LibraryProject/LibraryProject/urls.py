"""
URL configuration for LibraryProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from relationship_app.views import LibraryDetailView, LibrariesView
from relationship_app import views

from home import views as homeIndex


urlpatterns = [
    path(
        "admin/",
        admin.site.urls,
    ),
    path(
        "libraries/",
        LibrariesView.as_view(),
    ),
    path(
        "login/",
        LoginView.as_view(template_name="relationship_app/login.html"),
        name="login",
    ),
    path(
        "logout/",
        LogoutView.as_view(template_name="relationship_app/logout.html"),
        name="logout",
    ),
    path("register/", views.register, name="register"),
    path(
        "library/<int:pk>/",
        LibraryDetailView.as_view(),
    ),
    path(
        "books/",
        include("relationship_app.urls"),
    ),
    path("home/", homeIndex.index),
    path("", include("home.urls")),
]
