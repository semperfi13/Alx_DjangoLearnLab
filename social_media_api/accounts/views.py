from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import UserRegistrationSerializer
from rest_framework import permissions
from django.contrib.auth import get_user_model


# Create your views here.
class RegisterAPIView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data["token"])
        return Response({"token": token.key, "user_id": token.user_id})


class LogoutAPIView(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        return Response({"message": "Déconnexion réussie."}, status=200)


CustomUser = get_user_model()


class FollowUserAPIView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_follow = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            return Response(
                {"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND
            )

        # Add the user_to_follow to the authenticated user's following list
        request.user.following.add(user_to_follow)

        return Response(
            {"message": f"You are now following {user_to_follow.username}"},
            status=status.HTTP_200_OK,
        )


class UnfollowUserAPIView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_unfollow = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            return Response(
                {"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND
            )

        # Remove the user_to_unfollow from the authenticated user's following list
        request.user.following.remove(user_to_unfollow)

        return Response(
            {"message": f"You have unfollowed {user_to_unfollow.username}"},
            status=status.HTTP_200_OK,
        )


class UserListAPIView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        # Return a list of all users (except the current user)
        users = CustomUser.objects.all().exclude(id=request.user.id)
        usernames = [user.username for user in users]

        return Response({"users": usernames}, status=status.HTTP_200_OK)
