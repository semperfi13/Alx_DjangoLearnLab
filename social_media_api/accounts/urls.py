from django.contrib import admin
from django.urls import path, include
from .views import RegisterAPIView, LoginAPIView, LogoutAPIView
from .views import FollowUserAPIView, UnfollowUserAPIView

urlpatterns = [
    path("register/", RegisterAPIView.as_view(), name="api_register"),
    path("login/", LoginAPIView.as_view(), name="api_login"),
    path("logout/", LogoutAPIView.as_view(), name="api_logout"),
    path("follow/<int:user_id>/", FollowUserAPIView.as_view(), name="follow_user"),
    path(
        "unfollow/<int:user_id>/", UnfollowUserAPIView.as_view(), name="unfollow_user"
    ),
]
