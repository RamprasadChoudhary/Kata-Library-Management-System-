# Library Management System

This is a simple library management system that allows users to perform basic operations such as adding books, borrowing books, returning books, and viewing available books.

## Table of Contents
- [Setup](#setup)
- [Usage](#usage)
- [Running Tests](#running-tests)
- [Test Report](#test-report)
- [Project Structure](#project-structure)

## Setup

1. Clone the repository:
```bash
git clone https://github.com/RamprasadChoudhary/Kata-Library-Management-System-.git
cd Kata-Library-Management-System-
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install the required dependencies:
```bash
pip install pytest pytest-html
```

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

## Running Tests

To run the tests and generate a test report:

1. Ensure you're in the project root directory.
2. Run the following command:
```bash
python run_tests.py
```

Alternatively, you can use pytest directly:
```bash
pytest -v --html=test_report.html --self-contained-html
```

3. After running the tests, you'll see the test results in the console, and an HTML report will be generated.

## Test Report

The test report provides a comprehensive overview of the test suite execution. To view the report:

1. Locate the `test_report.html` file in the project root directory.
2. Open `test_report.html` in a web browser.

The report includes:
- Test results summary
- Detailed test case descriptions
- Pass/Fail statistics
- Test execution duration
- System information

Sample Test Output:

```plaintext
============================= test session starts ==============================
platform win32 -- Python 3.9.5, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
rootdir: /path/to/library_management_system
plugins: hypothesis-6.75.3, cov-4.1.0, html-3.1.1
collected 10 items

test_library.py::TestLibrary::test_add_book PASSED                    [ 10%]
test_library.py::TestLibrary::test_add_duplicate_book PASSED          [ 20%]
test_library.py::TestLibrary::test_borrow_book PASSED                 [ 30%]
test_library.py::TestLibrary::test_borrow_unavailable_book PASSED     [ 40%]
test_library.py::TestLibrary::test_borrow_nonexistent_book PASSED     [ 50%]
test_library.py::TestLibrary::test_return_book PASSED                 [ 60%]
test_library.py::TestLibrary::test_return_nonexistent_book PASSED     [ 70%]
test_library.py::TestLibrary::test_view_available_books PASSED        [ 80%]
test_library.py::TestLibrary::test_book_str_representation PASSED     [ 90%]

============================== 10 passed in 0.12s ==============================
Test report generated: test_report.html
```

## Project Structure

```plaintext
library_management_system/
│
├── library.py          # Main library management system implementation
├── test_library.py     # Test suite for the library system
├── run_tests.py        # Script to run tests and generate report
├── pytest.ini          # Pytest configuration file
└── README.md           # This file
```
