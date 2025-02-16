# Command: Update the title of “1984” to “Nineteen Eighty-Four” and save the changes

b = Book.objects.get(title=1984)
b.title = "Nineteen Eighty-Four"
b.save()
print(b.title)

OUTPUT
Nineteen Eighty-Four
