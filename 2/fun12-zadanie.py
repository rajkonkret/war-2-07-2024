# napisac funkcję, która przyjmuje argumenty age, first, last
# age powinien posiadać wartości domyślne
# z tych argumentów funkcja zbuduje słownik
# należy pobierać argumenty w pętli while
# zastosować "kalwisz ucieczki"
# ctrl / - cmd /

def build_dict(first, name, age=None):
    person = {'first': first, 'name': name}
    if age:  # jesli True
        person['age'] = age

    return person


print(bool(0))  # False
print(build_dict("Radek", "Kowalski", 56))
# {'first': 'Radek', 'name': 'Kowalski', 'age': 56}

while True:
    print("Podaj imię i nazwisko")
    print("Wpisz q by wyjść")

    f_name = input("imię")
    if f_name == 'q':
        break
    l_name = input("nazwisko")
    if l_name == 'q':
        break
    age = input("wiek")
    if age == 'q':
        break

    print(build_dict(f_name, l_name, age))
