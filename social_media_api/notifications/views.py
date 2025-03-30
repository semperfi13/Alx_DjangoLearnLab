from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Notification


class NotificationListAPIView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        notifications = Notification.objects.filter(recipient=request.user, read=False)
        data = [
            {
                "id": notif.id,
                "actor": notif.actor.username,
                "verb": notif.verb,
                "created_at": notif.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                "read": notif.read,
            }
            for notif in notifications
        ]

        return Response({"notifications": data}, status=status.HTTP_200_OK)


class MarkNotificationAsReadAPIView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, notification_id):
        notification = Notification.objects.filter(
            id=notification_id, recipient=request.user
        ).first()
        if notification:
            notification.read = True
            notification.save()
            return Response(
                {"message": "Notification marked as read."}, status=status.HTTP_200_OK
            )
        return Response(
            {"detail": "Notification not found."}, status=status.HTTP_404_NOT_FOUND
        )
