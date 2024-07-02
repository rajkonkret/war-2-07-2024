# lambda - skrocony zapis funkcji
# mozliwosc uzycia w miejscu deklaracji
# lambda domyslnie ma return
from functools import reduce, lru_cache


def liczymy(x, y):
    return x * y


print(liczymy(6, 7))  # 42

liczymy2 = lambda x, y: x * y

print(liczymy2(5, 3))  # 15

lista = [1, 2, 3, 4, 5, 6, 7, 8, 100, 200, 500]
# wypisaniu listy z wartosciami do potegi 2

lista2 = []
for i in lista:
    lista2.append(i ** 2)
print(lista2)  # [1, 4, 9, 16, 25, 36, 49, 64, 10000, 40000, 250000]


def zmien(x):
    return x ** 2


lista3 = []
for i in lista:
    lista3.append(zmien(i))

print([i ** 2 for i in lista])  # [1, 4, 9, 16, 25, 36, 49, 64, 10000, 40000, 250000]

# funkcje wyższego rzędu
# map(), filter(), reduce(), lru_cache()

# map() - weź kolejne elemnty z kolekcji, uruchom na nich funkcję
print(f"Zastosowanie map() {list(map(zmien, lista))}")
# Zastosowanie map() [1, 4, 9, 16, 25, 36, 49, 64, 10000, 40000, 250000]
print(f"Zastosowanie map() {list(map(lambda x: x ** 2, lista))}")
# Zastosowanie map() [1, 4, 9, 16, 25, 36, 49, 64, 10000, 40000, 250000]

# filter()

for i in lista:
    if i < 10:
        print(i)
# Użycie lambdy jako funkcji anonimowej
print(f"Użycie filter() {list(filter(lambda x: x < 5, lista))}")  # Użycie filter() [1, 2, 3, 4]
print(f"Użycie filter() {list(filter(lambda x: x < 45, lista))}")  # Użycie filter() [1, 2, 3, 4]
print(f"Użycie filter() {list(filter(lambda x: x > 45 and x < 200, lista))}")  # Użycie filter() [100]
print(f"Użycie filter() {list(filter(lambda x: 45 < x < 200, lista))}")  # Użycie filter() [100]
# Użycie filter() [1, 2, 3, 4, 5, 6, 7, 8]

r0 = {'miasto': "Kielce"}
r1 = {'miasto': "Kielce", "ZIP": "25-900"}
print(r0['miasto'])
print(r1['miasto'])
# print(r0['ZIP'])  # KeyError: 'ZIP'

print(r0.get('ZIP', "00-000"))  # 00-000
d_zip = lambda row: row.setdefault("ZIP", "00-000")
print(d_zip(r0))
print(d_zip(r1))
print(r0)
print(r1)
# {'miasto': 'Kielce', 'ZIP': '00-000'}
# {'miasto': 'Kielce', 'ZIP': '25-900'}

lata = [(2000, 29.7), (2001, 33.12), (2010, 32.92)]
print(max(lata))  # (2010, 32.92)
print(min(lata))  # (2000, 29.7)
print(max(lata, key=lambda c: c[1]))  # (2001, 33.12)
print(min(lata, key=lambda c: c[1]))  # (2000, 29.7)
print(max(map(lambda c: (c[1], c), lata)))  # (33.12, (2001, 33.12))
print(max(map(lambda c: c[1], lata)))  # 33.12
print(max(map(lambda c: (c[1], c[0]), lata)))  # (33.12, 2001)

# reduce()
"""
    reduce(function, iterable[, initial]) -> value

    Apply a function of two arguments cumulatively to the items of a sequence
    or iterable, from left to right, so as to reduce the iterable to a single
    value.  For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
    ((((1+2)+3)+4)+5).  If initial is present, it is placed before the items
    of the iterable in the calculation, and serves as a default when the
    iterable is empty.
    """
# 1 + 2 = 3
# 3 + 3 = 6
# 6 + 4 = 10
# 10 + 5 = 15
liczby = [1, 2, 3, 4, 5]
wynik = reduce(lambda a, b: a + b, liczby)
print(wynik)  # 15
wynik = reduce(lambda a, b: a * b, liczby)
print(wynik)  # 120


@lru_cache(maxsize=1000)
def fib_cashed(n):
    if n < 2:
        return n
    return fib_cashed(n - 1) + fib_cashed(n - 2)


print(fib_cashed(10))
print(fib_cashed.cache_info())
# CacheInfo(hits=8, misses=11, maxsize=1000, currsize=11)
print(fib_cashed(5))
print(fib_cashed.cache_info())
# CacheInfo(hits=9, misses=11, maxsize=1000, currsize=11)
# hits - ile razy uzyskał wynik nie musząc wykonywać obliczeń
# misses - tyle razy musiał na nowo obliczyć
fib_cashed.cache_clear()  # czyszczenie cache
print(fib_cashed.cashe_info())
