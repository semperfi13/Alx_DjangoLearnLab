from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from .views import LikePostAPIView, UnlikePostAPIView

router = DefaultRouter()
router.register(r"posts", PostViewSet)
router.register(r"comments", CommentViewSet)
from .views import FeedView

urlpatterns = [
    path("", include(router.urls)),
    path("feed/", FeedView.as_view(), name="feed"),
    path("<int:pk>/like/", LikePostAPIView.as_view(), name="like_post"),
    path("<int:pk>/unlike/", UnlikePostAPIView.as_view(), name="unlike_post"),
]
