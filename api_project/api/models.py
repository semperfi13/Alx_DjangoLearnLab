from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField(null=True)

    def __str__(self):
        return f"Title: {self.title} - Author: {self.author} - Published date: {self.published_date}"
