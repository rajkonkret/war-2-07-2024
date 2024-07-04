import pickle
from kl15 import Person

with open('dane.pickle', 'rb') as file:
    p = pickle.load(file)

print(p)  # [Person(first_name='Maciej', last_name='Nowak', id=2), Person(first_name='Jan', last_name='Kowalski', id=1)]

for person in p:
    print(person)
