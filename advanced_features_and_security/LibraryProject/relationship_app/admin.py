from django.contrib import admin
from .models import Author, Book, Library, Librarian

from .models import UserProfile

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)
admin.site.register(UserProfile)
