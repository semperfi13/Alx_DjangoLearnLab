from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publication_year = models.IntegerField()

    class Meta:
        permissions = [
            ("can_view", "can_view"),
            ("can_create", "can_view"),
            ("can_edit", "can_view"),
            ("can_delete", "can_view"),
        ]

    def __str__(self):
        return f"The title {self.title}, author {self.author}, and publication year {self.publication_year}."


class CustomUserManager(BaseUserManager):
    def create_user(
        self, email, date_of_birth, phone_number, profile_photo, password=None
    ):
        """
        Creates and saves a User with the given email, date of birth, and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            phone_number=phone_number,
            profile_photo=profile_photo,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, email, date_of_birth, phone_number, profile_photo, password=None
    ):
        """
        Creates and saves a superuser with the given email, date of birth, and password.
        """
        user = self.create_user(
            email=email,
            password=password,
            date_of_birth=date_of_birth,
            phone_number=phone_number,
            profile_photo=profile_photo,
        )
        user.is_staff = True  # Required for Django Admin
        user.is_superuser = True  # Required for Django Admin
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser):
    identifier = models.CharField(max_length=40, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    profile_photo = models.ImageField(upload_to="profile_photos/")

    USERNAME_FIELD = "identifier"
    REQUIRED_FIELDS = ["email", "phone_number", "date_of_birth", "profile_photo"]

    objects = CustomUserManager()  # Add custom manager
