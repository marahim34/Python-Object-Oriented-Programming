# Implement error handling for:
# - Invalid book ID when borrowing or returning a book.
# - Trying to borrow a book that is already borrowed.
# - Trying to return a book that is not borrowed.


class Book:
    def __init__(self, book_id, title, author, availability=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.availability = availability

    def borrow_book(self):
        if self.availability:
            self.availability = False
            return "This book has been borrowed successfully."
        else:
            return "Error: This book is already borrowed."

    def return_book(self):
        if not self.availability:
            self.availability = True
            return "You have successfully returned the book."
        else:
            return "Error: This book is not borrowed."


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
            return "Error: Invalid book ID. No book found with the given ID."
        return book.borrow_book()

    def return_book(self, book_id):
        book = self.find_book(book_id)
        if book is None:
            return "Error: Invalid book ID. No book found with the given ID."
        return book.return_book()


library = Library()

library.add_books(Book(1, "Pather Panchali", "Bibhutibhushan Bandyopadhyay"))
library.add_books(Book(2, "Shuvro", "Humayun Ahmed"))
library.add_books(Book(3, "Devdas", "Sarat Chandra Chattopadhyay"))

print(library.borrow_book(1))
print(library.borrow_book(1))
print(library.return_book(1))
print(library.return_book(1))
print(library.borrow_book(99))
print(library.return_book(99))
