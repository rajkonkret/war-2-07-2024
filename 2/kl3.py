from pprint import pprint


class ContactList(list['Contact']):
    def search(self, name):
        matching_contact = []
        for c in self:
            if name in c.name:
                matching_contact.append(c)
        return matching_contact


class Contact:
    all_contact = ContactList()  # pusta lista, wspolna dla wszystkich obiektów tej klasy, lista z naszej klasy ContactList

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contact.append(self)

    def __repr__(self):  # nadpisanie __repr__, nadpisuje __str__ jeśli nie zrobiliśmy własnego __str__
        return f"{self.name!r} {self.email!r}"


class Suplier(Contact):  # dziedziczenie po klasie Contact
    """
    Klasa dziedziczy po klasie Contakt
    """

    def order(self, order):
        print(f"{order} zamówiono od {self.name}")


class Friend(Suplier):
    """
    Klasa dziedziczy po Suplier
    """

    def __init__(self, name, email, phone='000000000'):
        super().__init__(name, email)  # super() w konstruktorze obowiązkowe
        self.phone = phone

    def __repr__(self):  # nadpisanie __repr__, nadpisuje __str__ jeśli nie zrobiliśmy własnego __str__
        return f"{self.name!r} {self.email!r}, +48{self.phone!r}"


c1 = Contact("Adam", "admin@wp.pl")
print(c1)  # Adam admin@wp.pl
c2 = Contact("Radek", "radek@wp.pl")
c3 = Contact("Tomek", "tomek@wp.pl")
print(c1.all_contact)  # [Adam admin@wp.pl, Radek radek@wp.pl, Tomek tomek@wp.pl]
print(c3.all_contact)  # [Adam admin@wp.pl, Radek radek@wp.pl, Tomek tomek@wp.pl]
s1 = Suplier("Marek", "marek@onet.pl")
print(s1.all_contact)
print(s1.all_contact)  # [Adam admin@wp.pl, Radek radek@wp.pl, Tomek tomek@wp.pl, Marek marek@onet.pl]
s1.order("kawa")
# kawa zamówiono od Marek
print(c1.all_contact.search("Radek"))  # [Radek radek@wp.pl]
lista = ContactList()
lista.append(s1)
print(lista)  # [Marek marek@onet.pl]
print(lista.search("Marek"))  # [Marek marek@onet.pl]

f1 = Friend("Kasia", 'kasia@wp.pl')
print(f1)
print(f1.all_contact)
f1.order("herbata")
# Kasia kasia@wp.pl, +48000000000
# [Adam admin@wp.pl, Radek radek@wp.pl, Tomek tomek@wp.pl, Marek marek@onet.pl, Kasia kasia@wp.pl, +48000000000]
# herbata zamówiono od Kasia
f2 = Friend("Zeneke", "Zenek@bialystok.pl", "678908765")
print(f2.all_contact)  # [Adam admin@wp.pl, Radek radek@wp.pl,
# Tomek tomek@wp.pl, Marek marek@onet.pl,
# Kasia kasia@wp.pl, +48000000000,
# Zeneke Zenek@bialystok.pl, +48678908765]
print(Friend.__mro__)
# (<class '__main__.Friend'>, <class '__main__.Suplier'>, <class '__main__.Contact'>, <class 'object'>)
pprint(f1.all_contact)
# [Adam admin@wp.pl,
#  Radek radek@wp.pl,
#  Tomek tomek@wp.pl,
#  Marek marek@onet.pl,
#  Kasia kasia@wp.pl, +48000000000,
#  Zeneke Zenek@bialystok.pl, +48678908765]
# po dodaniu !r łądniej wypisuje stringi
# ['Adam' 'admin@wp.pl',
#  'Radek' 'radek@wp.pl',
#  'Tomek' 'tomek@wp.pl',
#  'Marek' 'marek@onet.pl',
#  'Kasia' kasia@wp.pl, +48'000000000',
#  'Zeneke' Zenek@bialystok.pl, +48'678908765']
