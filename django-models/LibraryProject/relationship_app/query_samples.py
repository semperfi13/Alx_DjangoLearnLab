# Query all books by a specific author.

from relationship_app.models import Book, Library, Librarian, Author

# create

author = Author.objects.create(name="Ali Ben")
author.save()

book = Book.objects.create(title="1984", author=author)
book.save()

library = Library.objects.create(name="Semperfi Library", books=book)
library.save()

librarian = Librarian.objects.create(name="Karim Adeyemi", library=library)
librarian.save()

# Query all books by a specific author.

author = Author.objects.get(name="Ali Ben")
books = Book.objects.get(author=author)


# List all books in a library.

library = Library.objects.get(name="Semperfi Library")
all_books = library.books.all()

# Retrieve the librarian for a library.

librarian = Librarian.objects.get(library=library)
