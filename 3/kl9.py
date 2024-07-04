# stworzyc system zarzadzania biblioteką , który umożliwia dodanie ksiązek, wypozyczanie, zwracanie
# klasa Book, Library
# obsłużyć błędy
# dodać user który bedzie miał ksiązki jakie wypożyczył
# Book -> title, author, isbn
# Library -> lista ksiązek, lista wypozyczonych

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __repr__(self):
        return f"\'Author: {self.author!r}, Tytuł: {self.title!r}, ISBN: {self.isbn!r}\'"


class Library:
    def __init__(self):
        self.dostepne_ksiazki = []
        self.wypozyczone_ksiazki = []

    def fun_dodaj_ksiazke(self, book: "Book"):
        self.dostepne_ksiazki.append(book)

    def fun_ksiazki_do_wypozyczenia(self):
        return self.dostepne_ksiazki

    def fun_ksiazki_wypozyczone(self):
        return self.wypozyczone_ksiazki

    def fun_wypozycz_ksiazke(self, isbn):
        for book in self.dostepne_ksiazki:
            if book.isbn == isbn:
                self.dostepne_ksiazki.remove(book)
                self.wypozyczone_ksiazki.append(book)
                return book
        raise Exception("Nie ma takiej ksiązki")

    def fun_zwroc_ksiazke(self, isbn):
        for book in self.wypozyczone_ksiazki:
            if book.isbn == isbn:
                self.dostepne_ksiazki.append(book)
                self.wypozyczone_ksiazki.remove(book)
                return True
        raise Exception("Ksiązka nie z naszej biblioteki")


biblioteka = Library()
while True:
    print("""
    1. Dodaj ksiązkę
    2. Wypożycz ksiązkę
    3. Pokaż dostępne
    4. Pokaż wypożyczone
    5. Zwróc ksiązkę
    6. Koniec
    """)

    odp = input("Podaj opcje")
    if odp == "1":
        autor = input("Podaj autora")
        title = input("Podaj tytuł")
        isbn = input("Podaj numer ISBN")
        biblioteka.fun_dodaj_ksiazke(Book(title, autor, isbn))
        print("Ksiązka została dodana")
    elif odp == "2":
        isbn = input("Podaj ISBN książki, którą chcesz wypożyczyć")
        book = biblioteka.fun_wypozycz_ksiazke(isbn)
        print(f"Ksiązka {book} została wypożyczona")
    elif odp == "3":
        print(f"Dostępne ksiązki {biblioteka.fun_ksiazki_do_wypozyczenia()}")
    elif odp == "4":
        print(f"Wypożyczone ksiązki {biblioteka.fun_ksiazki_wypozyczone()}")
    elif odp == "5":
        isbn = input("Podaj ISBN książki, którą chcesz zwrócic")
        book = biblioteka.fun_zwroc_ksiazke(isbn)
        if book:
            print("Ksiazka zostala zwrócona")
    elif odp == "6":
        break
