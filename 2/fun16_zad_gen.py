# stworzenie raportu, przetworzenie danych
# generator danych - za pomocą generatora wygenerować dane
# wykorzystac dekorator do pomiaru czasu operacji
# storzyć raport, zmierzyć czas
import time


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Czas wykonania funkcji {func.__name__}: {execution_time}")

        return result

    return wrapper


def generator_danych(dane):
    for element in dane:
        yield element


def przetworz_dane(dane):
    return [element for element in dane if element % 2 == 0]


@measure_time
def stworz_raport(dane):
    for element in generator_danych(dane):
        print(f"Raport dla systemu {element}")


dane = range(100_000)
pr_dane = przetworz_dane(dane)
stworz_raport(pr_dane)
