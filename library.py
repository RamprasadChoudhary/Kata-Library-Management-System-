class Book:
    def __init__(self, isbn, title, author, year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.is_available = True

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year}) [ISBN: {self.isbn}]"
class BookNotAvailable(Exception):
    pass

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if any(existing_book.isbn == book.isbn for existing_book in self.books):
            raise ValueError("Book with this ISBN already exists")
        self.books.append(book)
    
    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.is_available:
                    book.is_available = False
                    return
                else:
                    raise BookNotAvailable("This book is not available for borrowing.")
        raise ValueError("Book not found in the library.")
    
    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                book.is_available = True
                return
        raise ValueError("Book not found in the library.")
    
    def view_available_books(self):
        return [book for book in self.books if book.is_available]