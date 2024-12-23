# In the constructor of the Book class, initialize the attributes.
# Insert the Book object into book_list using the method entry_book().
# This part will be done manually, i.e., no need for a menu option.


class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author


class Library:
    book_list = []

    def entry_book(self, book_id, title, author):
        book = Book(book_id, title, author)
        self.book_list.append(book)

    def display_books(self):
        books = ""
        for book in Library.book_list:
            books += f"Book Id = {book.book_id}, Title: {book.title}, Author: {book.author}\n"
        return books


library = Library()
library.entry_book(1, "Pather Panchali", "Bibhutibhushan Bandyopadhyay")
library.entry_book(2, "Shuvro", "Humayun Ahmed")
library.entry_book(3, "Devdas", "Sarat Chandra Chattopadhyay")


books = library.display_books()
print(books)
