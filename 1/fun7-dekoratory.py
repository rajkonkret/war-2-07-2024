# dekoratory - funkcje , które dodają nowe funkcjonalności do istniejących funkcji
# dekoratory wykorystują zasadę funkcji wewnętrznej

def dekor(funk):
    def wew():
        print("Funkcja wewnętrzna jako dekorator")
        return funk()  # zwraca wynik funkcji

    return wew  # zwracamy adres funkcji wewnętrznaj


@dekor  # dekorujemy funkcje
def nasza_funkcja():
    print("Funkcja, którą chcemy udekorować")


nasza_funkcja()
# Funkcja wewnętrzna jako dekorator
# Funkcja, którą chcemy udekorować
