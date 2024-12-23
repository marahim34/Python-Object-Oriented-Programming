# Define a class Book with the following instance attributes:
# - book_id: Unique identifier for the book.
# - title: Title of the book.
# - author: Author of the book.
# - availability: A boolean indicating if the book is available for borrowing or not.


class Book:
    def __init__(self, book_id, title, author, availability):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.availability = availability

    def get_book_availability(self):
        if self.availability is True:
            return f"The book is available"
        else:
            return f"The book is not available"


book1 = Book(1, "1984", "George Orwell", True)
book2 = Book(2, "Brave New World", "Aldous Huxley", False)

print(book1.get_book_availability())
print(book2.get_book_availability())
