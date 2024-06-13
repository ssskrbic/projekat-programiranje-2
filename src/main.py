
from library import Library

def main():
    library = Library()

    while True:
        print("\n1. Dodaj knjigu")
        print("2. Pretraži knjige")
        print("3. Prikaz svih knjiga")
        print("4. Izmeni knjigu")
        print("5. Obriši knjigu")
        print("6. Izlaz")
        izbor = input("Izaberite opciju: ")

        if izbor == "1":
            title = input("Unesite naslov knjige: ")
            author = input("Unesite autora knjige: ")
            year = int(input("Unesite godinu izdavanja: "))
            genre = input("Unesite žanr knjige: ")
            library.add_book(title, author, year, genre)
            print("Knjiga je dodata!")
        elif izbor == "2":
            search_type = input("Pretraga po (naslov, autor, godina, žanr): ").lower()
            search_value = input(f"Unesite vrednost za {search_type}: ")
            if search_type == "godina":
                search_value = int(search_value)
            results = library.search_books(**{search_type: search_value})
            if results:
                for book in results:
                    print(f"Naslov: {book.title}, Autor: {book.author}, Godina: {book.year}, Žanr: {book.genre}")
            else:
                print("Nema rezultata pretrage.")
        elif izbor == "3":
            print(library.display_books())
        elif izbor == "4":
            old_title = input("Unesite naslov knjige koju želite da izmenite: ")
            new_title = input("Unesite novi naslov knjige (ostavite prazno za bez promene): ")
            new_author = input("Unesite novog autora knjige (ostavite prazno za bez promene): ")
            new_year = input("Unesite novu godinu izdavanja knjige (ostavite prazno za bez promene): ")
            new_genre = input("Unesite novi žanr knjige (ostavite prazno za bez promene): ")

            if new_year:
                new_year = int(new_year)
                
            success = library.edit_book(old_title, new_title, new_author, new_year, new_genre)
            if success:
                print("Informacije o knjizi su uspešno izmenjene!")
            else:
                print("Knjiga sa navedenim naslovom nije pronađena.")
                
        elif izbor == "5":
            title = input("Unesite naslov knjige koju želite da obrišete: ")
            success = library.delete_book(title)
            if success:
                print("Knjiga je uspešno obrisana!")
            else:
                print("Knjiga sa navedenim naslovom nije pronađena.")
        
        elif izbor == "6":
            break
        else:
            print("Nepoznata opcija. Pokušajte ponovo.")

if __name__ == "__main__":
    main()
