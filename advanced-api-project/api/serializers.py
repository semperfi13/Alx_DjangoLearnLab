from rest_framework import serializers
from .models import Book
from .models import Author
import datetime


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["name"]


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ["title", "publication_year", "author"]

    def validate(self, data):
        if data["publication_year"] > datetime.date.year:
            raise serializers.ValidationError("Date must not bet in the future.")

        return data
