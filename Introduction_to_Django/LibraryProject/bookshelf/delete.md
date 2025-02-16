# Command: Delete the book you created and confirm the deletion by trying to retrieve all books again

from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

Book.objects.all()

OUTPUT

<QuerySet []>
