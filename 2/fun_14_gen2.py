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
print(list(gen4))
