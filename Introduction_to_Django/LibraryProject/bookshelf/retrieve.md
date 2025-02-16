# Command: Retrieve and display all attributes of the book you just created

b = Book.objects.get(title=1984)
print(books)

OUTPUT
<QuerySet [<Book: the title 1984, author George Orwell, and publication year 1949.>]>
