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
        
    def test_search_books_by_title(self):
        self.library.add_book("Lovac u zitu", "Dzerom Selindzer", 1951, "novela")
        results = self.library.search_books(title="Lovac u zitu")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Lovac u zitu")

    def test_search_books_by_author(self):
        self.library.add_book("Lovac u zitu", "Dzerom Selindzer", 1951, "novela")
        results = self.library.search_books(author="Dzerom Selindzer")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].author, "Dzerom Selindzer")

    def test_search_books_by_year(self):
        self.library.add_book("Lovac u zitu", "Dzerom Selindzer", 1951, "novela")
        results = self.library.search_books(year=1951)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].year, 1951)

    def test_search_books_by_genre(self):
        self.library.add_book("Lovac u zitu", "Dzerom Selindzer", 1951, "novela")
        results = self.library.search_books(genre="novela")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].genre, "novela")

    def test_search_books_no_match(self):
        self.library.add_book("Lovac u zitu", "Dzerom Selindzer", 1951, "novela")
        results = self.library.search_books(title="knjiga ne postoji")
        self.assertEqual(len(results), 0)
        
    def test_edit_book(self):
        self.library.add_book("Lovac u zitu", "Dzerom Selindzer", 1951, "novela")
        success = self.library.edit_book("Lovac u zitu", new_title="Na Drini cuprija", new_year=1945)
        self.assertTrue(success)
        self.assertEqual(self.library.books[0].title, "Na Drini cuprija")
        self.assertEqual(self.library.books[0].year, 1945)

    def test_edit_book_no_match(self):
        self.library.add_book("Lovac u zitu", "Dzerom Selindzer", 1951, "novela")
        success = self.library.edit_book("nepostojeca knjiga", new_title="New Title")
        self.assertFalse(success)
        
    def test_delete_book(self):
        self.library.add_book("Lovac u zitu", "Dzerom Selindzer", 1951, "novela")
        success = self.library.delete_book("Lovac u zitu")
        self.assertTrue(success)
        self.assertEqual(len(self.library.books), 0)

    def test_delete_book_no_match(self):
        self.library.add_book("Lovac u zitu", "Dzerom Selindzer", 1951, "novela")
        success = self.library.delete_book("nepostojeca knjiga")
        self.assertFalse(success)
        
if __name__ == "__main__":
    unittest.main()