# Library Management System

This is a simple library management system that allows users to perform basic operations such as adding books, borrowing books, returning books, and viewing available books.

## Setup

1. Clone the repository: git clone `<repository-url>`
cd library_management_system

```plaintext
2. Install the required dependencies:
```

pip install pytest  


## Running Tests

To run the tests, execute the following command in the project root directory: pytest test_library.py



## Usage

The `Library` class in `library.py` provides the following methods:

- `add_book(book)`: Add a new book to the library
- `borrow_book(isbn)`: Borrow a book from the library
- `return_book(isbn)`: Return a borrowed book to the library
- `view_available_books()`: View all available books in the library

Example usage:

```python
from library import Library, Book

# Create a library
library = Library()

# Add books
book1 = Book("1234567890", "Python Programming", "John Doe", 2023)
book2 = Book("0987654321", "Data Structures", "Jane Smith", 2022)
library.add_book(book1)
library.add_book(book2)

# Borrow a book
library.borrow_book("1234567890")

# View available books
available_books = library.view_available_books()
for book in available_books:
    print(f"{book.title} by {book.author}")

# Return a book
library.return_book("1234567890")

I'll guide you through creating a Library Management System using Python, following Test-Driven Development (TDD) principles and clean coding practices. We'll use pytest for testing. Let's go through this step-by-step.

Step 1: Set up the project

First, let's create a new directory for our project and initialize a Git repository:

```shellscript
mkdir library_management_system
cd library_management_system
git init
```

Now, let's create a README.md file:

```shellscript
echo "# Library Management System" > README.md
git add README.md
git commit -m "Initial commit with README"
```

Step 2: Set up the testing environment

Install pytest if you haven't already:

```shellscript
pip install pytest
```

Now, let's create our test file `test_library.py`:

```python
# test_library.py
import pytest
from library import Library, Book, BookNotAvailable

def test_add_book():
    library = Library()
    book = Book("1234567890", "Test Book", "Test Author", 2023)
    library.add_book(book)
    assert len(library.books) == 1
    assert library.books[0] == book

# Commit this file
```

Commit this file:

```shellscript
git add test_library.py
git commit -m "Add test for adding books"
```

Step 3: Implement the add_book feature

Create the `library.py` file:

```python
# library.py
class Book:
    def __init__(self, isbn, title, author, year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.is_available = True

class BookNotAvailable(Exception):
    pass

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

# Commit this file
```

Commit the changes:

```shellscript
git add library.py
git commit -m "Implement add book feature"
```

Run the tests:

```shellscript
pytest test_library.py
```

Step 4: Add test for borrowing books

Update `test_library.py`:

```python
# test_library.py
# ... (previous code)

def test_borrow_book():
    library = Library()
    book = Book("1234567890", "Test Book", "Test Author", 2023)
    library.add_book(book)
    library.borrow_book("1234567890")
    assert not book.is_available
    with pytest.raises(BookNotAvailable):
        library.borrow_book("1234567890")

# Commit this change
```

Commit the changes:

```shellscript
git add test_library.py
git commit -m "Add test for borrowing books"
```

Step 5: Implement the borrow_book feature

Update `library.py`:

```python
# library.py
# ... (previous code)

class Library:
    # ... (previous code)

    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.is_available:
                    book.is_available = False
                    return
                else:
                    raise BookNotAvailable("This book is not available for borrowing.")
        raise ValueError("Book not found in the library.")

# Commit this change
```

Commit the changes:

```shellscript
git add library.py
git commit -m "Implement borrow book feature"
```

Run the tests:

```shellscript
pytest test_library.py
```

Step 6: Add test for returning books

Update `test_library.py`:

```python
# test_library.py
# ... (previous code)

def test_return_book():
    library = Library()
    book = Book("1234567890", "Test Book", "Test Author", 2023)
    library.add_book(book)
    library.borrow_book("1234567890")
    library.return_book("1234567890")
    assert book.is_available

# Commit this change
```

Commit the changes:

```shellscript
git add test_library.py
git commit -m "Add test for returning books"
```

Step 7: Implement the return_book feature

Update `library.py`:

```python
# library.py
# ... (previous code)

class Library:
    # ... (previous code)

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                book.is_available = True
                return
        raise ValueError("Book not found in the library.")

# Commit this change
```

Commit the changes:

```shellscript
git add library.py
git commit -m "Implement return book feature"
```

Run the tests:

```shellscript
pytest test_library.py
```

Step 8: Add test for viewing available books

Update `test_library.py`:

```python
# test_library.py
# ... (previous code)

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

# Commit this change
```

Commit the changes:

```shellscript
git add test_library.py
git commit -m "Add test for viewing available books"
```

Step 9: Implement the view_available_books feature

Update `library.py`:

```python
# library.py
# ... (previous code)

class Library:
    # ... (previous code)

    def view_available_books(self):
        return [book for book in self.books if book.is_available]

# Commit this change
```

Commit the changes:

```shellscript
git add library.py
git commit -m "Implement view available books feature"
```

Run the tests:

```shellscript
pytest test_library.py
```

Step 10: Update README.md

Update the README.md file with instructions on how to set up and run the project:

```markdown
# Library Management System

This is a simple library management system that allows users to perform basic operations such as adding books, borrowing books, returning books, and viewing available books.

## Setup

1. Clone the repository:
```

git clone `<repository-url>`
cd library_management_system

```plaintext

2. Install the required dependencies:
```

pip install pytest

```plaintext

## Running Tests

To run the tests, execute the following command in the project root directory:

```

pytest test_library.py

```plaintext

## Usage

The `Library` class in `library.py` provides the following methods:

- `add_book(book)`: Add a new book to the library
- `borrow_book(isbn)`: Borrow a book from the library
- `return_book(isbn)`: Return a borrowed book to the library
- `view_available_books()`: View all available books in the library

Example usage:

```python
from library import Library, Book

# Create a library
library = Library()

# Add books
book1 = Book("1234567890", "Python Programming", "John Doe", 2023)
book2 = Book("0987654321", "Data Structures", "Jane Smith", 2022)
library.add_book(book1)
library.add_book(book2)

# Borrow a book
library.borrow_book("1234567890")

# View available books
available_books = library.view_available_books()
for book in available_books:
    print(f"{book.title} by {book.author}")

# Return a book
library.return_book("1234567890")
```

## Test Report

To generate a test report, run:

```plaintext
pytest test_library.py --html=report.html
```

This will create an HTML report of the test results in `report.html`.

```plaintext

Commit the changes:

```bash
git add README.md
git commit -m "Update README with setup and usage instructions"
```