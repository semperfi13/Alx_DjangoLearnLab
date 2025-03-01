from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import Book, CustomUser


class BookAdmin(admin.ModelAdmin):
    list_filter = ("title", "author", "publication_year")
    search_fields = ("title", "author")


class CustomUserAdmin(BaseUserAdmin):
    # Custom forms
    form = UserChangeForm
    add_form = UserCreationForm

    # Fields to display in the user list
    list_display = [
        "email",
        "identifier",
        "phone_number",
        "date_of_birth",
        "is_staff",
        "is_superuser",
    ]
    list_filter = ["is_staff", "is_superuser", "email"]

    fieldsets = [
        (None, {"fields": ["email", "identifier", "password"]}),
        (
            "Personal Info",
            {"fields": ["date_of_birth", "phone_number", "profile_photo"]},
        ),
        (
            "Permissions",
            {"fields": ["is_staff", "is_superuser", "groups", "user_permissions"]},
        ),
    ]

    # Fields used when adding a user
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": [
                    "email",
                    "identifier",
                    "date_of_birth",
                    "phone_number",
                    "profile_photo",
                    "password1",
                    "password2",
                ],
            },
        ),
    ]

    search_fields = ["email", "identifier", "phone_number"]
    ordering = ["email"]
    filter_horizontal = ["groups", "user_permissions"]


# Register models in Django admin
admin.site.register(Book, BookAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
