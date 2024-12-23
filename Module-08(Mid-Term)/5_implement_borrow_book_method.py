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
