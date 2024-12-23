# Implement error handling for:
# - Invalid book ID when borrowing or returning a book.
# - Trying to borrow a book that is already borrowed.
# - Trying to return a book that is not borrowed.


class Book:

    def __init__(self, book_id, title, author, availability):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.availability = availability

    def borrow_book(self):
        if self.availability is True:
            self.availability = False
            return "This book has been borrowed successfully"
        else:
            return "This book is already borrowed"

    def returning_book(self):
        if self.availability is False:
            self.availability = True
            return "You have successfully returned the book"
        else:
            return "This book is available for borrowing"


class Library:
    def __init__(self):
        self.books = []

    def add_books(self, book):
        self.books.append(book)

    def find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
            return None

    def borrow_book(self, book_id):
        book = self.find_book(book_id)
        if book is None:
            return "Error: Invalid Input"
        else:
            return book.borrow_book()

    def return_book(self, book_id):
        book = self.find_book(book)
        if book is None:
            return "Error: Invalid book ID."
        return book.returning_book()
