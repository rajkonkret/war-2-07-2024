# lazy - leniwy
lista = [1, 2, 3, 4, 5]
iterator = iter(lista)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
# 1
# 2
# 3
# 4
print("Zrób coś")
print(next(iterator))


# Zrób coś
# 5

class Count:
    def __init__(self, lows, high):
        self.current = lows
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


print("-----")
counter = Count(1, 5)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
# -----
# 1
# 2
# 3
# 4
print(next(counter))  # 5
print(next(counter))  # StopIteration
