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
