class Knjiga:
    def __init__(self, naslov, autor, godina_izdavanja, žanr):
        self.naslov = naslov
        self.autor= autor
        self.godina_izdavanja=godina_izdavanja
        self.žanr=žanr
    def display_info(self):
        return f'{self.naslov}, {self.autor}, {self.godina_izdavanja}, {self.žanr}'