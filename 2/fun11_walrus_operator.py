# walrus operator - operator morsa
name = "Radek"
if name == "Radek":
    print(f"Twoje imię to {name}")
# Twoje imię to Radek

# podstawia i porównuje
if name := "Tomek":  # walrus operator
    print(f"Twoje imię to {name}")
# Twoje imię to Tomek


przekaski = ['hotdog', 'pizza', 'hamburger', 'frytki']
prompt = "Wybierz swoją przekąskę"
print(przekaski)
print(type(przekaski))  # <class 'list'>

# while True:
#     choice = input(prompt)
#     if choice in przekaski:
#         break
#     print("Nie ma i co mi zrobisz")
#
# print(f"Twój wybór {choice}")
# while (choice := input(prompt)) not in przekaski:
#     if choice == 'exit':
#         break
#     print("Nie ma")
# print(f"Twój wybór {choice}")

name = "Radek"
n = len(name)
if n > 3:
    print(n)

if (n := len(name)) > 3:
    print(n)


def process(value):
    return value * 2


value = 10
result = process(value)
print(f"Processed result: {result}")  # Processed result: 20
