from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=250)
    publication_year = models.IntegerField()

    # author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="author")
    # Author: {self.author.name},
    def __str__(self):
        return f"Title: {self.title},  Publisher: {self.publication_year}"
