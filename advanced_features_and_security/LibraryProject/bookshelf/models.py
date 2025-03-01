from django.db import models
from django.contrib.auth.models import AbstractBaseUser


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"the title {self.title}, author {self.author}, and publication year {self.publication_year}."


class User(AbstractBaseUser):
    identifier = models.CharField(max_length=40, unique=True)
    USERNAME_FIELD = "identifier"
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    profile_photo = models.ImageField()
    REQUIRED_FIELDS = ["date_of_birth", "profile_photo", "email", "phone_number"]
