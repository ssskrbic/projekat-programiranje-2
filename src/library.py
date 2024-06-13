

from book import Book

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, year, genre):
        book = Book(title, author, year, genre)
        self.books.append(book)

    def display_books(self):
        if not self.books:
            return "Biblioteka je prazna."
        else:
            books_info = []
            for book in self.books:
                books_info.append(f"Naslov: {book.title}, Autor: {book.author}, Godina: {book.year}, Žanr: {book.genre}")
            return "\n".join(books_info)
    
    def search_books(self, title=None, author=None, year=None, genre=None):
        results = []
        for book in self.books:
            if (title and book.title == title) or \
               (author and book.author == author) or \
               (year and book.year == year) or \
               (genre and book.genre == genre):
                results.append(book)
        return results
