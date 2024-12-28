import pytest
from library import Library, Book, BookNotAvailable

def test_add_book():
    library = Library()
    book = Book("1234567890", "Test Book", "Test Author", 2023)
    library.add_book(book)
    assert len(library.books) == 1
    assert library.books[0] == book

def test_borrow_book():
    library = Library()
    book = Book("1234567890", "Test Book", "Test Author", 2023)
    library.add_book(book)
    library.borrow_book("1234567890")
    assert not book.is_available
    with pytest.raises(BookNotAvailable):
        library.borrow_book("1234567890")

def test_return_book():
    library = Library()
    book = Book("1234567890", "Test Book", "Test Author", 2023)
    library.add_book(book)
    library.borrow_book("1234567890")
    library.return_book("1234567890")
    assert book.is_available

def test_view_available_books():
    library = Library()
    book1 = Book("1234567890", "Test Book 1", "Test Author 1", 2023)
    book2 = Book("0987654321", "Test Book 2", "Test Author 2", 2022)
    library.add_book(book1)
    library.add_book(book2)
    library.borrow_book("1234567890")
    available_books = library.view_available_books()
    assert len(available_books) == 1
    assert available_books[0] == book2