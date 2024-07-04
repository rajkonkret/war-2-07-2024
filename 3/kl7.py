# mixin
class Printer:
    def print_message(self, message):
        print(f"Drukowanie wiadomości {message}")


class Scanner:
    def sca_document(self):
        print("Skanowanie dokumentu")
        return 'Zawartość dokumentu'


class MultifunctionDevice(Printer, Scanner):
    def photocopy(self):
        content = self.sca_document()
        self.print_message(content)


printer = Printer()
printer.print_message("Komunikat")

scanner = Scanner()
wynik = scanner.sca_document()
print(wynik)
# Drukowanie wiadomości Komunikat
# Skanowanie dokumentu
# Zawartość dokumentu

device = MultifunctionDevice()
device.photocopy()

print(MultifunctionDevice.__mro__)
# Skanowanie dokumentu
# Drukowanie wiadomości Zawartość dokumentu
# (<class '__main__.MultifunctionDevice'>, <class '__main__.Printer'>, <class '__main__.Scanner'>, <class 'object'>)
