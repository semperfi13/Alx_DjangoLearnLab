from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from bookshelf.models import User


class BookAdmin(admin.ModelAdmin):
    list_filter = ("title", "author", "publication_year")
    search_fields = ("title", "author")


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ["email", "date_of_birth"]
    list_filter = ["email"]
    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["date_of_birth"]}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "date_of_birth", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email"]
    filter_horizontal = []


admin.site.register(Book, BookAdmin)
admin.site.register(User, UserAdmin)
