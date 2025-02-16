# Command: Retrieve and display all attributes of the book you just created

books =Book.objects.all()
print(books)

OUTPUT
<QuerySet [<Book: the title 1984, author George Orwell, and publication year 1949.>]>
