import unittest
from library import Library

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()

    def test_add_book(self):
        self.library.add_book("Lovac u zitu", "Dzerom Selindzer", 1951, "novela")
        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(self.library.books[0].title, "Lovac u zitu")
        self.assertEqual(self.library.books[0].author, "Dzerom Selindzer")
        self.assertEqual(self.library.books[0].year, 1951)
        self.assertEqual(self.library.books[0].genre, "novela")

    def test_display_books_empty(self):
        result = self.library.display_books()
        self.assertEqual(result, "Biblioteka je prazna.")

    def test_display_books(self):
        self.library.add_book("Lovac u zitu", "Dzerom Selindzer", 1951, "novela")
        self.library.add_book("Put oko sveta za 80 dana", "Zil Vern", 1872, "fikcija")
        result = self.library.display_books()
        expected = "Naslov: Lovac u zitu, Autor: Dzerom Selindzer, Godina: 1951, Žanr: novela\n" \
                   "Naslov: Put oko sveta za 80 dana, Autor: Zil Vern, Godina: 1872, Žanr: fikcija"
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()