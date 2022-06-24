
"""
# Class-Inheritence
class BookShelf:
    def __init__(self, qunatity):
        self.quantity = qunatity

    def __str__(self):
        return f"This bookself contain {self.quantity} nos. of book"

# bookself = BookShelf(1500)
# print (bookself)

class Book(BookShelf):
    def __init__(self, name, quantity):
        super().__init__(quantity)
        self.name = name

book = Book("Harry Potter", 120)
print(book)

"""
# Class-Composition

class BookShelf:
    def __init__(self, *books):
        self.kitab = books

    def __str__(self):
        return f"bookshlef have {len(self.kitab)} types of books"

class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return F"Book {self.name}"

book = Book("Harry Potter")
book1 = Book("Fifty shades of Grey")

shelf = BookShelf(book,book1)
print(shelf)