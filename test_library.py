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