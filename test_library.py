import pytest
from library import Library, Book, BookNotAvailable

class TestLibrary:
    @pytest.fixture
    def library(self):
        return Library()

    @pytest.fixture
    def sample_book(self):
        return Book("1234567890", "Test Book", "Test Author", 2023)

    def test_add_book(self, library, sample_book):
        """Test adding a book to the library"""
        library.add_book(sample_book)
        assert len(library.books) == 1
        assert library.books[0] == sample_book

    def test_add_duplicate_book(self, library, sample_book):
        """Test adding a duplicate book"""
        library.add_book(sample_book)
        duplicate_book = Book("1234567890", "Test Book", "Test Author", 2023)
        with pytest.raises(ValueError, match="Book with this ISBN already exists"):
            library.add_book(duplicate_book)

    def test_borrow_book(self, library, sample_book):
        """Test borrowing an available book"""
        library.add_book(sample_book)
        library.borrow_book("1234567890")
        assert not sample_book.is_available

    def test_borrow_unavailable_book(self, library, sample_book):
        """Test borrowing an unavailable book"""
        library.add_book(sample_book)
        library.borrow_book("1234567890")
        with pytest.raises(BookNotAvailable):
            library.borrow_book("1234567890")

    def test_borrow_nonexistent_book(self, library):
        """Test borrowing a book that doesn't exist"""
        with pytest.raises(ValueError, match="Book not found in the library"):
            library.borrow_book("nonexistent")

    def test_return_book(self, library, sample_book):
        """Test returning a borrowed book"""
        library.add_book(sample_book)
        library.borrow_book("1234567890")
        library.return_book("1234567890")
        assert sample_book.is_available

    def test_return_nonexistent_book(self, library):
        """Test returning a book that doesn't exist"""
        with pytest.raises(ValueError, match="Book not found in the library"):
            library.return_book("nonexistent")

    def test_view_available_books(self, library):
        """Test viewing available books"""
        book1 = Book("1234567890", "Test Book 1", "Test Author 1", 2023)
        book2 = Book("0987654321", "Test Book 2", "Test Author 2", 2022)
        library.add_book(book1)
        library.add_book(book2)
        library.borrow_book("1234567890")
        available_books = library.view_available_books()
        assert len(available_books) == 1
        assert available_books[0] == book2

    def test_book_str_representation(self, sample_book):
        """Test string representation of a book"""
        expected = "Test Book by Test Author (2023) [ISBN: 1234567890]"
        assert str(sample_book) == expected