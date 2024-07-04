# hermetyzacja, enkapsulacjia

class Boat:
    """"
    Klasa łódka
    """

    def __init__(self, model, year):
        self.model = model
        self.year = year
        self.__speed = 0  # pole prywatne

    def sail(self):
        self.__speed += 10

    def speedometer(self):
        print(f"Speed in knots {self.__speed}")


boat = Boat("Maxus", 2023)
boat.sail()
boat.sail()
boat.sail()
boat.sail()
# po oznaczeniu pola jako prywatne
# AttributeError: 'Boat' object has no attribute '__speed'
# print(boat.__speed)  # 40
boat.speedometer()  # Speed in knots 40
boat.__speed = 0  # to doda pole o tej nazwie ale zasieg publiczny
boat.speedometer()  # Speed in knots 40
