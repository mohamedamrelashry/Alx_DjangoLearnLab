book = Book.objects.get(title="1984")
print("✅ Retrieved:", book.title, book.author, book.publication_year)

