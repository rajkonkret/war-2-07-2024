# klasy - element programowania obiektowego
# hiberncja, polimorfizm, dziedziczenie i abstrakcja
# klasa to szablon, opis, schemat, stempel
# obiekt - instancja kalsy, odcisk stempla, ciasto wg przepisu,
# element zbudowany wg wytycznych z klasa
# Klasa nakreśla minimum cech i funkcji dla obiektu

import math


class MyFirstClass:
    """
    Klasa w Pythonie, opisująca punkty w przestrzeni x i y
    """

    def __init__(self, x=0, y=0):
        """
        Funkcja inicjalizująca (konstruktor)
        :param x:
        :param y:
        """

        # self - obiekt na którym wykonywane są działania
        # self.x = x
        # self.y = y
        self.move(x, y)

    def move(self, x: int, y: int) -> None:
        """
        Funkcja przemieszcza punkt we wskazane miejsce

        :param x:
        :param y:
        :return: None
        """
        self.x = x
        self.y = y

    def reset(self):
        self.move(0, 0)

    def calculate(self, other: "MyFirstClass") -> float:
        """
        Obliczanie odległości między punktami w przestrzeni Euklidesowej
        :param other:
        :return:
        """
        return math.hypot(self.x - other.x, self.y - other.y)

    def __str__(self):  # opis obiektu
        return f"{self.x, self.y}"

    def __repr__(self):  # reprezentacja obiektu
        return f"Point({self.x}, {self.y})"


print(MyFirstClass.__doc__)
# print(print.__doc__)

ob = MyFirstClass()
print(ob)  # <__main__.MyFirstClass object at 0x000001AD75CF39B0>
# Po nadpisaniu metody __str__ obiekt wypisze się tak (0, 0)
print(type(ob))  # <class '__main__.MyFirstClass'>
# odczyt pól obiektu
print(ob.x)  # 0
print(ob.y)  # 0
ob.move(45, 78)
print(ob)  # (45, 78)
ob.reset()
print(ob)  # (0, 0)
ob2 = MyFirstClass(79, 45)
print(ob2)  # (79, 45)
print(ob.calculate(ob2))  # 90.91754506144565

lista = [ob, ob2]
print(lista)
# [<__main__.MyFirstClass object at 0x000001EE0666E2D0>,
# <__main__.MyFirstClass object at 0x000001EE0666EDE0>]
# po nadpisaniu metody __repr__
# [Point(0, 0), Point(79, 45)]
for p in lista:
    print(p)
