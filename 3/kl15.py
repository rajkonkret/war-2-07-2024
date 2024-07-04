# class Person:
#     def __init__(self, fn, ln, id):
#         self.fn = fn
#         self.ln = ln
#         self.id = id
#
#
# p1 = Person("Jan", "Kowalski", 1)
# print(p1)  # <__main__.Person object at 0x00000282F923D6D0>
import pickle
from dataclasses import dataclass


# dataclass - klasy przechowujące dane

@dataclass
class Person:
    first_name: str
    last_name: str
    id: int


p1 = Person("Jan", "Kowalski", 1)
print(p1)  # Person(first_name='Jan', last_name='Kowalski', id=1)

p2 = Person("Maciej", "Nowak", 2)
print(p2)  # Person(first_name='Maciej', last_name='Nowak', id=2)
people = [p2, p1]
print(people)
# [Person(first_name='Maciej', last_name='Nowak', id=2), Person(first_name='Jan', last_name='Kowalski', id=1)]

with open("dane.pickle", "wb") as stream:
    pickle.dump(people, stream)
