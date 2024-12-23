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
