class MyError(Exception):
    def __init__(self, message, err_code):
        super().__init__(message)
        self.err_code = err_code


class MyValueError(MyError):
    def __init__(self, message):  # klasa inicjalizujaca (konstruktor)
        super().__init__(message, err_code=100)  # obowiązkowo z kalsy nadrzednej -> super()


class MyTypeError(MyError):
    def __init__(self, message):
        super().__init__(message, err_code=200)


def my_function(x: int, y: int):
    if not isinstance(x, int):
        raise MyTypeError("x must be integer")
    if not isinstance(y, int):
        raise MyTypeError("y must be integer")
    if y == 0:
        raise MyValueError("y cannot be zero")

    return x / y


try:
    result = my_function(4, 5)
    # result = my_function(4, 0)
    result = my_function("a", 0)
except MyValueError:
    print("MyValueError")
except MyTypeError:
    print("MyTypeError")
else:
    print(f"Wynik działania {result}")
finally:
    print("Obliczenia zakończone")
