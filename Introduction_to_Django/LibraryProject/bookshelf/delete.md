# Command: Delete the book you created and confirm the deletion by trying to retrieve all books again

b = Book.objects.get(title="Nineteen Eighty-Four")
b.delete()

Book.objects.all()

OUTPUT

<QuerySet []>
