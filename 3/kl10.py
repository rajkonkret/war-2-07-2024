from abc import abstractmethod, ABC


class Counter(ABC):
    def __init__(self, values=0):
        self.values = values

    def increment(self, by=1):
        self.values += by

    @abstractmethod  # oznaczenie metody jako abstrakcyjna
    def drukuj(self):
        pass


class BoundedCounter(Counter):
    MAX = 100

    def __init__(self, values):
        if values > self.MAX:
            raise ValueError(f"Wartość nie może być większa od {self.MAX}")
        super().__init__(values)

    def drukuj(self):
        print("Drukuje", self.values)


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