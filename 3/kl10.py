from abc import abstractmethod, ABC


class Counter(ABC):
    def __init__(self, values=0):
        self.values = values

    def increment(self, by=1):
        self.values += by

    @abstractmethod  # oznaczenie metody jako abstrakcyjna
    def drukuj(self):
        pass

    @classmethod  # metoda zwraca obiekt klasy Counter
    def from_counter(cls, counter):
        return cls(counter.values)

    @staticmethod  # metoda statyczna, nie wymaga obiektu tej klasy
    def from_string():
        print("Metoda statyczna")


class BoundedCounter(Counter):
    MAX = 100

    def __init__(self, values):
        if values > self.MAX:
            raise ValueError(f"Wartość nie może być większa od {self.MAX}")
        super().__init__(values)

    def drukuj(self):
        print("Drukuje", self.values)


class NewCounter(Counter):
    """
    Klasa dziedziczy po Counter
    """


# TypeError: Can't instantiate abstract class Counter without an implementation for abstract method 'drukuj'
# po dodaniu @abstractmethod nie możemy tworzyc obiektów tej klasy
# metoda abstrakcyjna - nie ma ciałą, nic nie robi
# c1 = Counter()
# c1.increment()
# c1.drukuj()

bc = BoundedCounter(10)
bc.increment()
bc.drukuj()  # Drukuje 11

bc2 = BoundedCounter(30)
bc2.increment()
bc2.increment()
bc2.increment()
bc2.drukuj()
# Drukuje 11
# Drukuje 33


# obiekty są polimorficzne bo mają wspólne elementy
lista = [bc, bc2]
for i in lista:
    i.drukuj()
# TypeError: Can't instantiate abstract class NewCounter without an implementation for abstract method 'drukuj'
# NewCounter nie ma metody drukuj nadpisanej
# nc = NewCounter()

a = BoundedCounter.from_counter(bc)
print(a)
print(type(a))
# <__main__.BoundedCounter object at 0x000001BE841AE930>
# <class '__main__.BoundedCounter'>
a.drukuj()  # Drukuje 11

# uzycie metody statycznej, nie wymaga obiektu
BoundedCounter.from_string()
# Metoda statyczna
