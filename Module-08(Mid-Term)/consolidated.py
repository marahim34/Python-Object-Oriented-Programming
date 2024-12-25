# Problem 1:
# Define a class named Library with one class attribute named book_list.
# Initially, it should be an empty list. Create a class method entry_book()
# to insert an object of the Book class into book_list.


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    book_list = []

    @classmethod
    def entry_book(cls, title, author):
        book = Book(title, author)
        cls.book_list.append(book)

    @classmethod
    def display_books(cls):
        book_info = ""
        for book in cls.book_list:
            book_info += f"Title: {book.title}, Author: {book.author}\n"
        return book_info


library = Library()
library.entry_book("Gulliver's Travels", "Jonathan Swift")
library.entry_book("1984", "George Orwell")

# For retrieving all books from the book list
books = library.display_books()
print(books)

# For retrieving single book from the book_list with their index
book = library.book_list[0]
print(f"Title: {book.title}, Author: {book.author}")


# Problem - 2
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


# Problem - 3
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


# Problem - 4
# Add a method borrow_book() in the Book class that checks if the
# book is available for borrowing (i.e., the book’s availability is True).
# If so, change the availability to False.


class Book:
    def __init__(self, book_id, title, author, availability):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.availability = availability

    def borrow_book(self):
        if self.availability is True:
            self.availability = False
            return f"The book has been borrowed successfully."
        else:
            return f"The Book is already borrowed"


book1 = Book(1, "Pather Panchali", "Bibhutibhushan Bandyopadhyay", True)
book2 = Book(2, "Shuvro", "Humayun Ahmed", False)

book_Borrowed = book1.borrow_book()
print(book_Borrowed)

book_Borrowed = book2.borrow_book()
print(book_Borrowed)


# Problem - 5
# Add a method return_book() in the Book class that changes the availability of the book back to True when a book is returned.


class Book:
    def __init__(self, book_id, title, author, availability):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.availability = availability

    def borrow_book(self):
        if self.availability is True:
            self.availability = False
            return "The book has been borrowed successfully"
        else:
            return "The book is already borrowed"

    def return_book(self):
        if self.availability is False:
            self.availability = True
            return "The book is now returned and available for borrowing"
        else:
            return "The book is available for borrowing"


book1 = Book(1, "Pather Panchali", "Bibhutibhushan Bandyopadhyay", True)
book2 = Book(2, "Shuvro", "Humayun Ahmed", False)

book_Borrowed = book1.borrow_book()
print(book_Borrowed)

book_returned = book1.return_book()
print(book_returned)


# Problem - 6
# Add a method view_book_info() in the Book class to display the details of the book, including its book_id, title, author, and availability status.


class Book:
    all_books = []

    def __init__(self, book_id, title, author, availability_status):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.availability_status = availability_status

    @classmethod
    def add_books(cls, book_id, title, author, availability_status):
        book = Book(book_id, title, author, availability_status)
        cls.all_books.append(book)

    @classmethod
    def view_book_info(cls):
        books = ""
        for book in cls.all_books:
            books += (
                f"Book Id = {book.book_id}, Title: {book.title}, Author: {book.author}, "
                f"Availability Status: {'Available' if book.availability_status else 'Borrowed'}\n"
            )
        return books


Book.add_books(1, "Pather Panchali", "Bibhutibhushan Bandyopadhyay", True)
Book.add_books(2, "Shuvro", "Humayun Ahmed", False)
Book.add_books(3, "Devdas", "Sarat Chandra Chattopadhyay", True)

books = Book.view_book_info()
print(books)


# Problem - 7
class Book:
    def __init__(self, book_id, title, author, availability=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.availability = availability

    def borrow_book(self):
        if self.availability:
            self.availability = False
            return "The book has been borrowed successfully."
        else:
            return "The book is already borrowed."

    def return_book(self):
        if not self.availability:
            self.availability = True
            return "The book has been returned and is now available."
        else:
            return "The book is already available."


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def view_all_books(self):
        if not self.books:
            return "No books are available in the library."
        result = ""
        for book in self.books:
            result += f"ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Availability: {'Available' if book.availability else 'Borrowed'}\n"
        return result

    def borrow_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book.borrow_book()
        return "Book not found."

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book.return_book()
        return "Book not found."


library = Library()
library.add_book(Book(1, "Pather Panchali", "Bibhutibhushan Bandyopadhyay"))
library.add_book(Book(2, "Shuvro", "Humayun Ahmed"))
library.add_book(Book(3, "Devdas", "Sarat Chandra Chattopadhyay"))


def menu():
    while True:
        print("\nLibrary Menu:")
        print("1. View All Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Exit")
        try:
            user_input = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if user_input == 1:
            print("\nAll Books:")
            print(library.view_all_books())
        elif user_input == 2:
            try:
                book_id = int(input("Enter the ID of the book to borrow: "))
                print(library.borrow_book(book_id))
            except ValueError:
                print("Invalid input. Please enter a valid book ID.")
        elif user_input == 3:
            try:
                book_id = int(input("Enter the ID of the book to return: "))
                print(library.return_book(book_id))
            except ValueError:
                print("Invalid input. Please enter a valid book ID.")
        elif user_input == 4:
            print("Exiting the menu. Goodbye!")
            break
        else:
            print("Invalid input. Please select a valid option.")


menu()


# Problem - 8
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


# problem - 9
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
