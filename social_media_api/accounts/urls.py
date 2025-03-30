from django.contrib import admin
from django.urls import path, include
from .views import RegisterAPIView, LoginAPIView, LogoutAPIView

urlpatterns = [
    path("register/", RegisterAPIView.as_view(), name="api_register"),
    path("login/", LoginAPIView.as_view(), name="api_login"),
    path("logout/", LogoutAPIView.as_view(), name="api_logout"),
]
