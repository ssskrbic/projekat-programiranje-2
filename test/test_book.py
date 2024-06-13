

import unittest
from book import Book

class TestBook(unittest.TestCase):
    def test_book_initialization(self):
        book = Book("Lovac u zitu", "Dzerom Selindzer", 1951, "novela")
        self.assertEqual(book.title, "Lovac u zitu")
        self.assertEqual(book.author, "Dzerom Selindzer")
        self.assertEqual(book.year, 1951)
        self.assertEqual(book.genre, "novela")

if __name__ == "__main__":
    unittest.main()