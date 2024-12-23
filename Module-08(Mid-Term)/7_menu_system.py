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
