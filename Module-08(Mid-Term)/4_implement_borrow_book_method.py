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
