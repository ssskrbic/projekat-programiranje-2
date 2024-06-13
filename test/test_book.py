

import unittest
from book import Book

class TestBook(unittest.TestCase):
    def test_book_initialization(self):
        book = Book("Harry Potter", "J.K. Rowling", 1997, "Fantasy")
        self.assertEqual(book.title, "Harry Potter")
        self.assertEqual(book.author, "J.K. Rowling")
        self.assertEqual(book.year, 1997)
        self.assertEqual(book.genre, "Fantasy")

if __name__ == "__main__":
    unittest.main()