# zrobić dekorator, który zamienia wynik funkcji na duże litery
# funkcja która zwraca tekst
# dekorator, który zamieni wynik tej funkcji na duze litery
def uppercase_decorator(func):
    # *args - dowolna ilość  po pozycji
    # **kwargs - dowolna ilosć nazwanych (słownikowych)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()  # zamiana na duże litery

    return wrapper


@uppercase_decorator
def greeting():
    return "Hello World!!!"


print(greeting())  # HELLO WORLD!!!
