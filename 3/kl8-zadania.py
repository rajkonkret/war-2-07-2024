# stworzenie ksiązki telefonicznej z wykoryzstaniem pętli while
# dodaj kontakt, usun kontakt, wyszukaj kontakt, wyswietl kontakt

# stworzyc system zarzadzania biblioteką , który umożliwia dodanie ksiązek, wypozyczanie, zwracanie
# klasa Book, Library
# obsłużyć błędy
# dodać user który bedzie miał ksiązki jakie wypożyczył

contacts = {}
while True:
    print(f"""
    1. Dodaj kontakt
    2. Usuń kontakt
    3. Wyszukaj kontakt
    4. Wyświetl kontakt
    5. Koniec
""")
    try:
        odp = input("Wybierz opcję")
        if odp == "1":
            name = input("Podaj imie kontaktu")
            number = input("Podaj numer telefon (tylko cyfry")
            if not number.isdigit():
                raise ValueError("Numer telefonu powinien zawierac cyfry!")  # rzucenie wyjątku
            else:
                contacts[name.lower()] = number
                print(f"Kontakt został dodany")
        elif odp == "2":
            name = input("Podaj imię kontaktu do usunięcia")
            if name in contacts:
                # del contacts[name.lower()]
                contacts.pop(name.lower())
                print(f"Kontakt {name} został usunęty")
            else:
                print(f"Nie znaleziono kontaktu o imieniu {name}")
        elif odp == "3":
            name = input("Podaj imię do wyszukania")
            if name.lower() in contacts:
                print(f"Kontakt {name.capitalize()} nr telefonu: {contacts[name.lower()]}")
            else:
                print(f"Nie znaleziono kontaktu o imieniu {name}")
        elif odp == "4":
            print(f"Lista kontaktów: {contacts}")
        elif odp == "5":
            break
        else:
            print("Błedny wybór")
    except Exception as e:
        print("Bład", e)
