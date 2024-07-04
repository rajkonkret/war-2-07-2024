class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    @classmethod
    def z_nazwy_pelnej(cls, nazwa_pelna):
        imie, nazwisko = nazwa_pelna.split()
        return cls(imie, nazwisko)


osoba1 = Osoba("Jan", "Kowalski")
print(osoba1.imie, osoba1.nazwisko)  # Jan Kowalski
print(osoba1.imie, osoba1.nazwisko, sep="")  # JanKowalski

a, b = "Anna Nowak".split()  # rozdziela string na pojedyncze elemnty
osoba2 = Osoba(a, b)
print(osoba2.imie, osoba2.nazwisko)

osoba3 = Osoba.z_nazwy_pelnej("Magda Tkacz")
print(osoba3.imie, osoba3.nazwisko)
# Jan Kowalski
# JanKowalski
# Anna Nowak
# Magda Tkacz
