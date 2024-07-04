# stworzyc słownik z funkcją, która zwraca najdłuższy klucz w słowniku
# longest_key

class LongestKeyDict(dict):
    def longest_key(self):
        longest = None
        for key in self:  # tu dostajemy klucze
            if longest is None or len(key) > len(longest):
                longest = key

        return longest


dictionary = LongestKeyDict()
dictionary.longest_key()
# wzorzec o długosci 0
# bierzemy słowo
# sprawdzamy czy jest dłuze od wzorca
# jesli dłuzsze niz wzorzezc to zapisz do wzorca to słowo
dictionary['tomasz'] = 45
dictionary['abraham'] = 7
dictionary['zen'] = 12
print(dictionary.longest_key())  # abraham
