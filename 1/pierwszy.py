import sys

print("Radek")
print('Radek')  # str
print(type("Radek"))  # <class 'str'>

# PEP8 - zasady czystego kodu
# ctrl alt l - automatyczne formatowanie kodu
# Reformat code Ctr+Alt+L
imie = "Radek"
print(f'Nazywam się {imie}')  # Nazywam się Radek
# f - string format, wstawiamy wartosci w nawiasach {}
print("Nazywam się %s" % imie)  # Nazywam się Radek
print("Nazywam się {}".format(imie))  # Nazywam się Radek
print("Nazywam się", imie)  # Nazywam się Radek

# typowanie dynamiczne - typ danych wnioskowany na podstawie zawartości
imie = "Radek"
print(type(imie))
imie = 90
print(type(imie))  # <class 'int'> całkowite
imie: str = "Tomek"  # :str - podpowiedz (hint)
print(imie)
imie = 78
print(imie)  # 78

print(10 + 10)  # 20
print('10' + '10')  # 1010 - konkatenacja, łączenie stringów
# silne typowanie - nie zamienia sam typów w kontekscie działania
# print('10' + 10)  # TypeError: can only concatenate str (not "int") to str
# musimy jawnie zamienic
print(int('10') + 10)  # 20 int() - rzutowanie na int
print('10' + str(10))  # 1010 str() - rzutowanie na str

print(23.45)
print(type(23.45))  # <class 'float'>
print(0.1 + 0.2)  # bład zaokrąglenai przy float 0.30000000000000004
print(sys.float_info)
# sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021,
#                min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)

lista = []  # pusta lista
lista.append("Radek")
print(lista)  # ['Radek']

krotka = 1, 2, 3
print(krotka)  # (1, 2, 3)
print(type(krotka))  # <class 'tuple'> niezmienna, niemutowalna

zbior = set()  # pusty zbiór
zbior.add("Radek")
print(zbior)  # {'Radek'}
print(type(zbior))  # <class 'set'>

dictionary = {"name": "Radek"}
print(dictionary)  # {'name': 'Radek'} odwzorowuje jsona
print(type(dictionary))  # <class 'dict'>

logiczna = True
# może byc True lub False

for i in range(10):  # 0..9
    print(i)

licznik = 0
while licznik < 10:
    licznik += 1  # licznik = licznik + 1
    print(licznik)

if logiczna:
    print("Prawda")  # Prawda
else:
    print("Fałsz")

# match case - od python 3.10
odp = input("Podaj imie")  # str
match odp:
    case "Radek":
        print("ok")
    case _:  # odpowiednik else, wartość domyślna
        print("No trudno")
