# generatory - generuje wartość dla danego argumentu
# przy następnym wywołaniu poda wartość dla kolejnego argumentu
# zapamietuje gdzie się zatrzymał
def kwadrat(n):
    for x in range(n):
        print(x ** 2)


kwadrat(5)


def kwadrat2(n):
    for x in range(n):
        yield x ** 2  # odsyła wynik, zapamietuje pozycje gdzie skończyło


kwa = kwadrat2(5)
print(kwa)  # <generator object kwadrat2 at 0x000001C9A6C03780>

print(next(kwa))  # pobiera kolejny element
print(next(kwa))  # pobiera kolejny element
print(next(kwa))  # pobiera kolejny element
print(next(kwa))  # pobiera kolejny element
# 0
# 1
# 4
# 9
print("Zrób cokolwiek")
lista = []
lista.append("123456")
print(lista)
# Zrób cokolwiek
# ['123456']
print(next(kwa))  # 16
# print(next(kwa))  # StopIteration - wyczerpany generator

kwa2 = kwadrat2(10)
kwa3 = kwadrat2(20)

print(next(kwa2))
print(next(kwa3))
print(next(kwa2))
print(next(kwa3))

print(list(kwa3))
# [4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]
