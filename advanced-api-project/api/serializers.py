from rest_framework import serializers
from .models import Book
from .models import Author
import datetime


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["name"]


class BookSerializer(serializers.ModelSerializer):
    # author = AuthorSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ["title", "publication_year"]

    def validate(self, data):
        d = datetime.date.today()
        year = d.strftime("%Y")
        if data["publication_year"] > int(year):
            raise serializers.ValidationError("Date must not bet in the future.")

        return data
