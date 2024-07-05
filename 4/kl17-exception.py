# print(2 / 0)
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\war-2-07-2024\4\kl17-exception.py", line 1, in <module>
#     print(2 / 0)
#           ~~^~~
# ZeroDivisionError: division by zero
# raise ZeroDivisionError
# Traceback (most recent call last):
#   File "C:\Users\CSComarch\PycharmProjects\war-2-07-2024\4\kl17-exception.py", line 7, in <module>
#     raise ZeroDivisionError
# ZeroDivisionError
# możemy tworzyć własne wyjątki tworząc klaśe dziedziczącą z Exception
class MyEception(Exception):
    def __init__(self, message):
        super().__init__(message)


try:
    x = int(input("Podaj liczbę calkowitą większą od zera"))
    if x < 0:
        raise MyEception("Liczba musi być większa od zera")
except MyEception:
    print("Wartość musi być większa od zera")
except Exception as e:  # łapie wszystkie pozostałe wyjątki
    print("Bład", e)