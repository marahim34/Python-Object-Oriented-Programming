# Make the attributes (such as book_id, title, author, availability)
# as protected/private as possible using Python’s class mechanisms.
# This will ensure that these attributes cannot be accessed directly outside the class.


class Book:

    def __init__(self, book_id, title, author, availability=True):
        self.__book_id = book_id
        self.__title = title
        self.__author = author
        self.__availability = availability

    def get_book_id(self):
        return self.__book_id

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def is_available(self):
        return self.__availability

    def set_availability(self, availability):
        self.__availability = availability


class Library:
    def __init__(self):
        self.__books = []  # Private list to store book objects

    def add_books(self, book):
        self.__books.append(book)

    def display_books(self):
        for book in self.__books:
            availability = "Available" if book.is_available() else "Not Available"
            print(
                f"ID: {book.get_book_id()}, Title: {book.get_title()}, "
                f"Author: {book.get_author()}, Status: {availability}"
            )

    def lend_book(self, book_id):
        for book in self.__books:
            if book.get_book_id() == book_id and book.is_available():
                book.set_availability(False)
                print(f"The book '{book.get_title()}' has been lent.")
                return
        print("The book is either not available or doesn't exist.")

    def return_book(self, book_id):
        for book in self.__books:
            if book.get_book_id() == book_id and not book.is_available():
                book.set_availability(True)
                print(f"The book '{book.get_title()}' has been returned.")
                return
        print("The book is either already available or doesn't exist.")


library = Library()

library.add_books(Book(1, "Pather Panchali", "Bibhutibhushan Bandyopadhyay"))
library.add_books(Book(2, "Shuvro", "Humayun Ahmed"))
library.add_books(Book(3, "Devdas", "Sarat Chandra Chattopadhyay"))

print("Books in the Library:")
library.display_books()

print("\nLending a book:")
library.lend_book(2)

print("\nBooks in the Library after lending:")
library.display_books()

print("\nReturning a book:")
library.return_book(2)

print("\nBooks in the Library after returning:")
library.display_books()
