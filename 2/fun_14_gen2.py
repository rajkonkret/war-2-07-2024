from itertools import zip_longest

generator_1 = [x for x in range(5)]
print(generator_1)
print(type(generator_1))

generator_2 = (x for x in [1, 2, 3, 4, 5])
print(type(generator_2))  # <class 'generator'>
print(generator_2)  # <generator object <genexpr> at 0x000001E7F82ECE80>
print(next(generator_2))
print(next(generator_2))
print(next(generator_2))
print(next(generator_2))
print(next(generator_2))


def generator3():
    for x in [1, 2, 3, 4, 5]:
        yield x


g3 = generator3()
print(next(g3))
print(next(g3))
print(next(g3))


def gen4():
    i = 1
    while True:
        yield i * 1
        i += 1


g4 = gen4()
print(next(g4))
print(next(g4))
print(next(g4))
print(next(g4))
print(next(g4))


def fibo():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b


fib1 = fibo()
print(next(fib1))
print(next(fib1))
print(next(fib1))
print(next(fib1))
print(next(fib1))


def fibo_with_index(n):
    a, b = 0, 1
    for ind in range(n):
        yield ind, a
        a, b = b, a + b


# shift tab  -cofnięcie wciecia
fib2 = fibo_with_index(100)
print(next(fib2))
print(next(fib2))
print(next(fib2))
print(next(fib2))
print(next(fib2))
# (0, 0)
# (1, 1)
# (2, 1)
# (3, 2)
# (4, 3)

for i, n in fibo_with_index(10):  # (4, 3) -> (i,n) -> i, n
    print(f"Pozycja {i} Element {n}")
# Pozycja 0 Element 0
# Pozycja 1 Element 1
# Pozycja 2 Element 1
# Pozycja 3 Element 2
# Pozycja 4 Element 3
# Pozycja 5 Element 5
# Pozycja 6 Element 8
# Pozycja 7 Element 13
# Pozycja 8 Element 21
# Pozycja 9 Element 34

fibo3 = fibo_with_index(10)
print(list(fibo3))
print("----------")
for i in fibo3:
    print(i)
# list() wyczerpało generator, nie ma kolejnych elemntów
# [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8), (7, 13), (8, 21), (9, 34)]
# ----------

person = ['Radek', 'Tomek', 'Zenek', 'Agnieszka', 'Marta']
age = [34, 45, 23, 36]

# zip() - łączy kolekcje
for p, w in zip(person, age):
    print(p, w)
# Radek 34
# Tomek 45
# Zenek 23
# Agnieszka 36

zipped = zip_longest(person, age, fillvalue=None)
print(zipped)  # <itertools.zip_longest object at 0x000002576B8FD580>
lista = list(zipped)  # [('Radek', 34), ('Tomek', 45), ('Zenek', 23), ('Agnieszka', 36), ('Marta', None)]
# print(next(zipped))  # StopIteration
for item in lista:
    print(item)


# ('Radek', 34)
# ('Tomek', 45)
# ('Zenek', 23)
# ('Agnieszka', 36)
# ('Marta', None)


def counter(start=0):
    n = start
    while True:
        result = yield n
        print(result)  # Ok
        if result == 'q':
            break
        n += 1


c = counter(10)
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(c.send("Ok"))
try:
    print(c.send('q'))  # StopIteration
except StopIteration:
    print("Koniec")  # Koniec
