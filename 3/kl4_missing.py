# __missing__ - metoda wykonywana gdy nie ma klucza w słowniku


class DefaultDict(dict):
    def __missing__(self, key):
        return "default"


class AutoKeyDict(dict):  # dziedziczenie po dict
    def __missing__(self, key):
        self[key] = 0
        return key


class CaseInsesitiveDict(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            return self.get(key.lower())


d_python = {}  # pusty słownik pythonowy
# print(d_python['name'])  # KeyError: 'name'


d1 = DefaultDict()
print(type(d1))  # <class '__main__.DefaultDict'>
print(d1)  # {}
print(d1['name'])  # default

a1 = AutoKeyDict()
print(a1)
print(a1['imie'])
print(a1)
# {}
# None
# {'imie': 0}

csd = CaseInsesitiveDict()
csd['name'] = "Radek"
print(csd['NamE'])  # Radek
