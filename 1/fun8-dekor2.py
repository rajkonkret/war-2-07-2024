# zrobić dekorator, który zamienia wynik funkcji na duże litery
# funkcja która zwraca tekst
# dekorator, który zamieni wynik tej funkcji na duze litery
def uppercase_decorator(func):
    # *args - dowolna ilość  po pozycji
    # **kwargs - dowolna ilosć nazwanych (słownikowych)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()  # zamiana na duże litery

    return wrapper  # zwraca adres


def bold_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"\033[1m" + result + "\033[0m"

    return wrapper


@uppercase_decorator
def greeting():
    return "Hello World!!!"


print(greeting())  # HELLO WORLD!!!


# dekorator, który zamieni tekst na pogrubiony
# \033[1m włączenie pogrubienia
# \033[0m wyłaczenie pogrubienia
# \t tab
# \n nowa linia
# pobrac wynik funkcji
# zmienić na bold
@bold_decorator  # pogrubione
@uppercase_decorator  # RADEK
def greeting2(name):
    return name


print(greeting2("Radek"))
