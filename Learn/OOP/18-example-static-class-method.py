class Book():
    #below variables are property of the class
    TYPES = ("hardcover", "paperback")

print (Book.TYPES)
#######################
class Book():
    def __init__(self, name, book_type, weigh):
        self.name = name
        self.book_type = book_type
        self.weigh = weigh

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type} and weight of the book {self.weigh} kg>"

book = Book("Harry_Potter", "Hardcover", "1.6")
print(book)
#################################
#Factory
class Book():
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weigh):
        self.name = name
        self.book_type = book_type
        self.weigh = weigh

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type} and weight of the book {self.weigh} g>"

    @classmethod
    def hard(cls, name, page_weight):
        return Book(name, Book.TYPES[0], page_weight + 100)
    @classmethod
    def light(cls, name, page_weight):
        return Book(name, Book.TYPES[1], page_weight)


    


book = Book.hard("Harry Potter", 1500)
paper = Book.light("python 101", 900)
print(book)
print(paper)