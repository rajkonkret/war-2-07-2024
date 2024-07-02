# funkcja - wydzielony fragment kodu, można wywołąć w dowolnym momencie
# funkcja musi być najpierw zadeklarowana
# w miejscu deklaracji funkcja nie jest uruchamiana
# aby wywołąć funkcje trzeba ją wywołać

a = 10
b = 15


# deklaracja funkcji
def dodaj():
    print(a + b)


def dodaj2(a, b):
    print(a + b)


# to tylko podpowiedzi, to nie sprawdza typu
def odejmij(a: int, b: int, c=0):  # c - posiada wartość domyślną
    print(a - b - c)


def mnozenie(a, b):
    return a * b


# zwracanie wielu wartości
def mnozenie2(a, b):
    return a, b, a * b


# uruchomienie funkcji
# przekazywanie po pozycji
dodaj()  # 25
dodaj2(56, 78)  # 134
odejmij(6, 3, 2)
print(mnozenie(2, 5))
print(mnozenie2(6, 7))  # (6, 7, 42) wynik jako krotka

# przekazywanie po nazwie
odejmij(c=6, b=9, a=9)  # -6

print(mnozenie(4, 5) * mnozenie(9, 8))  # 1440
# print(dodaj() + dodaj())  # TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'

a = mnozenie2(5, 6)
print(a)  # (6, 7, 42)
x, y, z = a  # rozpakowanie krotki
print(f"Wynik {x} * {y} = {z}")  # Wynik 5 * 6 = 30
