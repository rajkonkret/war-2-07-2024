from functools import total_ordering


class MyNumber:
    def __init__(self, value):
        self.value = value


print(5 < 15)  # True
num1 = MyNumber(5)
num2 = MyNumber(15)

# print(num1 < num2)  # TypeError: '<' not supported between instances of 'MyNumber' and 'MyNumber'
print(num1.value < num2.value)  # True


@total_ordering  # automatycznie uzupełni pozostałe porównania
class MyNumber2:
    def __init__(self, value):
        self.value = value

    # <
    def __lt__(self, other):
        return self.value < other.value

    # ==
    def __eq__(self, other):
        return self.value == other.value


num3 = MyNumber2(5)
num4 = MyNumber2(15)
num5 = MyNumber2(15)
print(num3 < num4)  # True
print(num5 == num4)  # False, on porównał referencje (adres)
# żeby porównał obiekty jako wartości value musimy dopisać metodę __eq__
print(num5 == num4)  # true
print(num5 > num3)  # True
