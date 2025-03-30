from django.urls import path
from .views import NotificationListAPIView, MarkNotificationAsReadAPIView

urlpatterns = [
    path("", NotificationListAPIView.as_view(), name="notifications_list"),
    path(
        "<int:notification_id>/read/",
        MarkNotificationAsReadAPIView.as_view(),
        name="mark_notification_as_read",
    ),
]
